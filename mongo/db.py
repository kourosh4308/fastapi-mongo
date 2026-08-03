from pymongo import MongoClient


client = MongoClient('mongodb://pr-mongo-fastapi:27017/')

database = client['mydb']     #database name
users = database['player']   #collection name
