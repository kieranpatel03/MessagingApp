To run the website locally, execute the following commands:

```cd backend
pip3 install -r requirements.txt
python3 manage.py runserver 
```

```
cd .. 
cd frontend 
npm install
npm run serve 
```

The site consists of a main page which, when logged in, will show all the conversations the user is currently having. 

<div>
<img width="300" alt="Screenshot 2023-02-11 at 16 13 09" src="https://user-images.githubusercontent.com/45712533/218269553-db962e62-9b45-4fe1-99c2-b6aad3a6b6b1.png">
<img width="270" alt="Screenshot 2023-02-11 at 16 35 59" src="https://user-images.githubusercontent.com/45712533/218269774-3cb4277f-0d97-4a13-82ca-70b1f936ea51.png">
</div>

When a conversation is clicked, the messages are shown:

<img width="400" alt="Screenshot 2023-02-11 at 16 36 58" src="https://user-images.githubusercontent.com/45712533/218269810-32adf315-63a9-4655-892f-b503e8b345a2.png">
A message can be typed and sent and it will show up in the conversation.
