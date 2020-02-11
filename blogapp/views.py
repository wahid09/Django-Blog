from django.shortcuts import render, HttpResponse

def index(requset):
    return HttpResponse("<h1>Hello</h1>")