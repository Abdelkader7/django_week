from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render,redirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

from .logic_for_views import store_restaurant, get_restaurant, count_restaurant, get_users
from .connect_to_mongodb import get_count_from_mongo, db


#import matplotlib 
#matplotlib.use('TkAgg')

#from matplolib import pylab 



@login_required(login_url='')
def home_page_view_with_render(request):
    return render(request,"home_page.html", {"title_page": "Accueil"})

def in_client_group(user):
    if user:
        return user.groups.filter(name='clients').count() != 0
    return False

def in_restaurant_group(user):
    if user:
        return user.groups.filter(name='restaurants').count() != 0
    return False

@login_required(login_url='')
def redirection(request):
    return render(request,"redirection.html", {"title_page": "Error"})
    
@login_required(login_url='')
def carte(request):
    return render(request,"map.html", {"title_page": "Carte"})

@login_required(login_url='')
def graph(request):
    return render(request, "graph.html", {"title_page": "Graphique"}  )

def subscribe(request):
    if request.method == "POST":
       # print(request.POST)
       username = request.POST['identifiant']
       email = request.POST['email']
       password = request.POST['password']
       user = User.objects.create_user(username,email ,password )
       user.first_name = request.POST["nom"] 
       user.last_name = request.POST["prenom"] 

       return render(request, "home_page.html", {"title_page": "Inscription"})
    else:
        return render(request, "subscribe.html", {"title_page": "Inscription"})

@login_required(login_url='/login')
@user_passes_test(in_restaurant_group, login_url='/redirection')
def restaurant_registration(request): 
    nbre_restaurant = get_count_from_mongo(db=db, collection_name="restaurant")
    if request.method == "POST":
    
        restaurant_nom = request.POST["nom_restaurant"]
        restaurant_adresse = request.POST["adresse_restaurant"]
        
        if(store_restaurant(nom=restaurant_nom, adresse=restaurant_adresse, db=db, collection="restaurant")):
            return render(request, "restaurant_registration.html", {"title_page": "Enregistrement d'un restaurant",'message_success': "Restaurant enregistré !", 
                                                            "nbre_restaurant": nbre_restaurant })
        else:
            return render(request, "restaurant_registration.html", {"title_page": "Enregistrement d'un restaurant",'message_fail': "Restaurant déjà existant !", 
                                                            "nbre_restaurant": nbre_restaurant })

    return render(request, "restaurant_registration.html", {"title_page": "Enregistrement d'un restaurant", 
                                                            "nbre_restaurant": nbre_restaurant })


def restaurant_liste(request):
    liste_restaurants = get_restaurant(db=db, collection="restaurant")
    return render(request, "restaurant_liste.html", {"title_page": "Liste des restaurants", "liste_restaurants":liste_restaurants})

@login_required(login_url='')
@user_passes_test(in_client_group, login_url='/redirection')
def user_liste(request):
    return render(request, "user_liste.html", {"title_page": "Liste des utilisateurs",'users':get_users()})
