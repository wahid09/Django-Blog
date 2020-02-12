from django.shortcuts import render, HttpResponse

def index(requset):
    return render(requset, "index.html")


def getauthor(request, name):
    return render(request, "profile.html")

def getsingle(requset, id):
    return render(requset, "single.html")