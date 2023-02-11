from django.urls import path

from . import views

urlpatterns = [
    path('', views.get_data, name='get_data'),
    path('select', views.select_data, name='select_data'),
    path('insert', views.insert_data, name='insert_data'),
    path('retrieve', views.get_user, name='get_user'),
    path('create', views.create_user, name='create_user'),
]