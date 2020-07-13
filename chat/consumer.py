import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from Admin.models import Query_table
from django.core import serializers
from .data_analysis import text_mining
from django.db.models import Q
from .Similarity import demo

class ChatConsumer(WebsocketConsumer):
    asked_question=" "
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        self.asked_question = text_data_json['message']
        flag = text_data_json['flag']
        message = text_data_json['message']
        msg = 'not found'
        ans=''
        ans_id=''

        if flag == 0:
            print("In flag =0")
            t=None
            find_name = text_mining(message)
            name = find_name.identify_name()
            
            if(name == '0'):
                name = 'User'
                flag = 2
            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type' : 'chat_message',
                    'flag' : flag,
                    'answer':name,
                    'ans_id':ans_id,
                    'q':self.asked_question
                }
            )


        if flag == 1 :
            t=None
            obj = demo()
            for p in Query_table.objects.raw('select * from "Admin_query_table"'):
                r = obj.cosine_distance_wordembedding_method(p.quesion, self.asked_question)
                if t==None:
                    t = r
                    ans = p.answer
                    ans_id=p.id
                elif t < r:
                    t = r
                    ans = p.answer
                    ans_id=p.id

            hold = Query_table.objects.get(id = ans_id)
            hold.viewed = hold.viewed + 1
            hold.save() 

            # Send message to room group
            async_to_sync(self.channel_layer.group_send)(
                
                self.room_group_name,
                {
                    'type' : 'chat_message',
                    'flag' : flag,
                    'answer':ans,
                    'ans_id':ans_id,
                    'q':self.asked_question
                }
                
            )

    # Receive message from room group
    def chat_message(self, event):
        ans = event['answer']
        flag = event['flag']      
        ans_id = event['ans_id']  

        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'type' : 'chat_message',
            'flag' : flag,
            'answer':ans,
            'ans_id':ans_id,
            'q':self.asked_question
        }))



 
