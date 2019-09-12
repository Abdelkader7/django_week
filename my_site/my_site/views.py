from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .logic_for_views import store_restaurant, db


#import matplotlib 
#matplotlib.use('TkAgg')

#from matplolib import pylab 



def home_page_view(request):
    return HttpResponse('Hello World')

#@login_required
def home_page_view_with_render(request):
    return render(request,"home_page.html", {"title_page": "Accueil"})

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

#@login_required
def carte(request):
    return render(request,"map.html", {"title_page": "Carte"})


def graph(request):
    return render(request, "graph.html", {"title_page": "Graphique"}  )

def subscribe(request):
    if request.method == "POST":
       # print(request.POST)
       username = request.POST['identifiant']
       email = request.POST['email']
       password = request.POST['password']
       user = User.objects.create_user(username,email ,password )
       user.last_name = request.POST["nom"] 
       user.last_name = request.POST["prenom"] 

       return render(request, "home_page.html", {"title_page": "Inscription"})
    else:
        return render(request, "subscribe.html", {"title_page": "Inscription"})

def restaurant_registration(request): 
    if request.method == "POST":
        restaurant_nom = request.POST["nom_restaurant"]
        restaurant_adresse = request.POST["adresse_restaurant"]
        
        if(store_restaurant(nom=restaurant_nom, adresse=restaurant_adresse, db=db, collection="restaurant")):
            return render(request, "restaurant_registration.html", {"title_page": "Enregistrement d'un restaurant",'message_success': "Restaurant enregistré !"})
        else:
            return render(request, "restaurant_registration.html", {"title_page": "Enregistrement d'un restaurant",'message_fail': "Restaurant déjà existant !"})

    return render(request, "restaurant_registration.html", {"title_page": "Enregistrement d'un restaurant"})