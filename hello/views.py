from django.shortcuts import render
from django.http import HttpResponse
import datetime

def myview(request):
    now = datetime.datetime.now()
    return HttpResponse(now)
