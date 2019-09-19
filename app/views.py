from django.shortcuts import render
from django.http import HttpResponse
"""deal with request and data"""


def index(request):
    # pass the 'context' data to templates 
    context = {
        'message': 'Welcome my BBS',
        'players': ['勇者', '戦士', '魔法使い']
    } 
    # open templates/app/index.html on server
    return render(request, 'app/index.html', context)
