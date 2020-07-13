from django.shortcuts import render
from django.http import HttpResponse
from Admin.models import Query_table,list_unsat
from django.contrib import messages
from django.db.models import Q
# Create your views here.


def index(request):
    return render(request, 'chatpage.html')

def room(request, room_name):
    if(request.GET.get('flag')=="satisfied"):
        flag = request.GET.get('flag')
        qid= request.GET.get('qid')
        print(qid)
        save_qa=Query_table.objects.get(id=qid)
        save_qa.satisfied=save_qa.satisfied+1
        #save_qa=Query_table(questionID=6,satisfied=1,unsatisfied=1,viewed=1)
        try:
            save_qa.save()
            print('saved')
        except:
            print('Error')
    elif(request.GET.get('flag')=="unsatisfied"):
        flag = request.GET.get('flag')
        qid= request.GET.get('qid')
        userQ=request.GET.get('userQ')
        save_qa=Query_table.objects.get(id=qid)
        save_qa.unsatisfied=save_qa.unsatisfied+1
        save_unsat=list_unsat(question=userQ,dbqid=qid)
        try:
            save_qa.save()
            save_unsat.save()
            print('saved')
        except:
            print('Error')
    else:
        print("yeheh")

    return render(request, 'room.html', {
        'room_name': room_name
    })