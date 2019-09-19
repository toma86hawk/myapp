from django.shortcuts import render
from django.http import HttpResponse
"""deal with request and data"""


def index(request):
    # open templates/app/index.html on server
    return render(request, 'app/index.html')
