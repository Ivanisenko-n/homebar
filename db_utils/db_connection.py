from pymongo import MongoClient

def connect_to_mongodb():
    client = MongoClient("mongodb://bar_user:12345678@localhost:27017/")
    db = client["mydatabase"]
    return db

def create_alcohol_collection():
    db = connect_to_mongodb()
    collection = db["alcohol"]
    return collection

def create_cocktail_collection():
    db = connect_to_mongodb()
    collection = db["cocktail"]
    return collection

def create_category_collection():
    db = connect_to_mongodb()
    collection = db["category"]
    return collection