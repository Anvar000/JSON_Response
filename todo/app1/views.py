from django.http import HttpResponse
from django.shortcuts import render
import json

# Create your views here.


def home(request):
    data = open('response_data.json').read()
    return HttpResponse(data)
