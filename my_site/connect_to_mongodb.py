import pymongo

client = pymongo.MongoClient()
# Le nom de la DB est "restaurants" (si elle n'existe pas elle est créée)
db = client["restaurant"]

def get_count_from_mongo(db, collection_name):
    return(db[collection_name].find().count())