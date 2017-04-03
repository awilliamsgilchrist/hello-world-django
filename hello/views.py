from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.

def index(request):
    intCheck = int(time.time()) % 4
    responseString = ""
    if intCheck == 0:
        responseString = " north"
    elif intCheck == 1:
        responseString = " east"
    elif intCheck == 2:
        responseString = " south"
    else:
        responseString = " west"
    return HttpResponse("Hello World! I predict are currently " + responseString + " of Old Main")