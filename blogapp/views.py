from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import Author, Category, Artical
from django.contrib.auth import authenticate, login, logout

def index(requset):
    post = Artical.objects.all()
    context = {
        "post": post
    }
    return render(requset, "index.html", context)


def getauthor(request, name):
    return render(request, "profile.html")

def getsingle(requset, id):
    post = get_object_or_404(Artical, pk=id)
    first = Artical.objects.first()
    last = Artical.objects.last()
    related = Artical.objects.filter(category=post.category).exclude(id=id)
    context = {
        "post": post,
        "first": first,
        "last": last,
        "related": related
    }
    return render(requset, "single.html", context)

def getcategory(requset, name):
    cat = get_object_or_404(Category, name=name)
    post = Artical.objects.filter(category=cat.id)
    context={
        "post":post
    }
    return render(requset, "category_post.html", context)

def getlogin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            user = request.POST.get('user')
            password = request.POST.get('pass')
            auth = authenticate(request, username=user, password=password)
            if auth is not None:
                login(request, auth)
                return redirect('home')

    return render(request, "login.html")

def getlogout(request):
    logout(request)
    return redirect('login')