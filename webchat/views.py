#from django.forms import Input
from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from json import dumps
from webchat import answers

# Create your views here.

def home(request):
    
    return render(request,'index.html')
    
def add(request):

    qus=dict(request.GET)
    q=list(qus.keys())
    
    question=str(answers.user_in(q[0])).lower()
    print(question)
    answer=str(answers.ai_ans(question))
    '''
    dataDictionary ={'hello': 'World','geeks': 'forgeeks','ABC': 123,456: 'abc',
    14000605: 1,'list': ['geeks', 4, 'geeks'],'dictionary': {'you': 'can', 'send': 'anything', 3: 1}}
    #a="Hi"
    datajson=dumps(dataDictionary)
    print(datajson)

    return render(request,"index.html",{'data':datajson})'''
    a='ujjwal'
    response = {
        'key2' : answer,
    }

    return JsonResponse(response)
