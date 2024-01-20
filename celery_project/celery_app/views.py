from django.shortcuts import render
from django.http import HttpResponse
from .task import *
from .helper import *

# Create your views here.
def index(request):
   # checking simple sleepy function
    # sleepy.delay(10)

    # sending mail without celery -  takes usually 5-10 seconds 
    # send_mail_without_celery()

    # sending mail using celery - takes 1-2 seconds 
    send_mail_through_celery.delay()
    return HttpResponse("<h1> mail has been sent thhrough celery, </h1>")
    # return HttpResponse("<h1> mail has been sent without celery, </h1>")