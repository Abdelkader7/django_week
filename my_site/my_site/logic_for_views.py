import pymongo

client = pymongo.MongoClient()
# Le nom de la DB est "restaurants" (si elle n'existe pas elle est créée)
db = client["restaurant"]

# Le nom de la collection est "from_app" (si elle n'existe pas elle est créée)
# On affiche le nombre d'objets dans la DB dans la console lors du démarrage de l'appelle
print("{} questions in the DB".format(db["from_app"].count_documents({})))

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


    