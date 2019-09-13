import pymongo
from django.contrib.auth.models import User

client = pymongo.MongoClient()
# Le nom de la DB est "restaurants" (si elle n'existe pas elle est créée)
db = client["restaurant"]

print("{} restaurants in the DB".format(db["restaurant"].count_documents({})))

def store_restaurant(nom, adresse, db, collection):
    restaurant = {'restaurant_nom': nom,
                'restaurant_adresse': adresse }

    if(db[collection].find_one({"restaurant_nom" : nom}) == None):
        db["restaurant"].insert_one(restaurant)
        print("valeur enregistré")
        return True
    else:
        print("valeur déjà existante")
        return False
    return None

def get_restaurant(db, collection):
    liste_restaurant = list(db["restaurant"].find())
    return liste_restaurant


def count_restaurant(db, collection):
    liste_restaurant = db["restaurant"].find().count()
    return liste_restaurant
    
def get_users():
    users = User.objects.all()
    return users
