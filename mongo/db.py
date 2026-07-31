from pymongo import MongoClient


client = MongoClient('mongodb://pr-mongo-fastapi:27017/')

db = client['mydb']     #database name
users = db['player']   #collection name


