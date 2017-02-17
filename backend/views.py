#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<p>你好，世界!</p>")
# Create your views here.
