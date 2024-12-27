from pymongo import MongoClient
import os
MONGO_URI = os.getenv('MONGO_URI')
client = MongoClient(os.getenv(MONGO_URI))
db = client['twitter_trends'] 

def get_db():
    return db
