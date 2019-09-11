from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


#import matplotlib 
#matplotlib.use('TkAgg')

#from matplolib import pylab 



def home_page_view(request):
    return HttpResponse('Hello World')

@login_required
def home_page_view_with_render(request):
    return render(request,"home_page.html")

def login2(request):

   

    if request.method == "POST":
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
       # print(request.POST)
        #login_user = request.POST["login"]
        #password_user = request.POST["password"]
        #user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        #print(password_user)
    else:
        return render(request, "login.html")

@login_required
def carte(request):
    return render(request,"map.html")


def graph(request):
    return render(request, "graph.html")

def subscribe(request):
    if request.method == "POST":
       # print(request.POST)
       username = request.POST['identifiant']
       email = request.POST['email']
       password = request.POST['password']
       user = User.objects.create_user(username,email ,password )
       user.last_name = request.POST["nom"] 
       user.last_name = request.POST["prenom"] 

       return render(request, "home_page.html")
    else:
        return render(request, "subscribe.html")