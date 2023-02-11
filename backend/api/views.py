from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from api.models import Message
from django.contrib.auth.models import User
from datetime import datetime
from django.core.serializers.json import DjangoJSONEncoder
import json 
from itertools import groupby
from django.db.models import Count, Max
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt



def get_username(user_id):
    try:
        user = User.objects.get(id=user_id)
        return user.username.capitalize()
    except User.DoesNotExist:
        return 'Unknown'

# Create your views here.
def get_data(request):
    parameters = request.GET.dict()
    user_to = parameters['user_id']
    authorization = request.headers['Authorization']      
    user_logged = Token.objects.get(key=authorization).user.id #Authenticates the user
    message_list = Message.objects.filter(user_sent=user_logged, user_to=user_to) | Message.objects.filter(user_to=user_logged, user_sent=user_to) #Gets a list of the messages between the two users
    message_list = list(message_list.order_by('date_sent').values())
    messages = {
        'message_list': message_list,
        'message_to_name': get_username(user_id=user_to),
        'message_from_name': get_username(user_id=2),
        'message_to_id': user_to,
        'message_from_id': user_logged,
    }
    return HttpResponse(json.dumps(messages, cls=DjangoJSONEncoder)) #Sends the messages alongside the name and id of both users back as a response. 

    
def select_data(request):
    authorization = request.headers['Authorization']    
    user = Token.objects.get(key=authorization).user.id
    messages = Message.objects.filter(user_sent=user) | Message.objects.filter(user_to=user) #Gets all messages that a user has sent or received. 
    msg = {}
    for i in list(messages.values().order_by('-date_sent')): #groups the messages the user has receive/sent with the person it has received it from or sent it to. 
        if str(i['user_to']) == str(user):
            user_id = i['user_sent']
        elif str(i['user_sent']) == str(user):
            user_id = i['user_to']
        else:
            raise Exception("User unknown")
        try:
            if msg[user_id]['can_notif'] and user_id == i['user_sent']:
                if i['message_read']:
                    msg[user_id]['notifs'] += 1
                else:
                    msg[user_id]['can_notif'] = False
            elif user_id == i['user_sent']:
                msg[user_id]['can_notif'] = False
        except:
            msg[user_id] = {"last_message": i['message'], "last_date": i['date_sent'], "notifs": int(i['message_read']), "can_notif": i['message_read']}
    msg = list(map(lambda x : {"user_id": x[0], "user_name": get_username(x[0]), 'last_message': x[1]['last_message'], 'last_date': x[1]['last_date'], 'notifs': x[1]['notifs']}, list(msg.items()))) #Gets the last message the user sent/received with each user it has conversed with. 
    return HttpResponse(json.dumps(msg, cls=DjangoJSONEncoder))

@csrf_exempt
def get_user(request):
    if request.method == 'POST':
        parameters = json.loads(request.body)
    else:
        return HttpResponse(status=500)
    user = authenticate(**parameters)
    if not user:
        return HttpResponse("Incorrect username or password.", status=422)
    token, _ = Token.objects.get_or_create(user=user) 
    return HttpResponse(json.dumps({'token': token.key}), status=200) #Authenticates the user and then creates/gets a token and sends it back.

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        parameters = json.loads(request.body)
    else:
        return HttpResponse(status=500)
    user = User.objects.create_user(username=parameters['username'], password=parameters['password'])
    token, _ = Token.objects.get_or_create(user=user)
    return HttpResponse(json.dumps({'token': token.key}), status=200) #Cretaes a user and then creates a token and sends it back.

@csrf_exempt
def insert_data(request):
    if request.method == 'POST':
        parameters = json.loads(request.body)
    else:
        return HttpResponse(status=500)
    authorization = request.headers['Authorization']  
    user_sent = Token.objects.get(key=authorization).user.id
    Message.objects.create(user_sent=user_sent, user_to=parameters['user_to'], message=parameters['message'], message_read=False, date_sent=datetime.utcnow()) #creates a message in a conversation between two users. 
    return HttpResponse(status=204) 