from models.users_model import User
from mongo.db import users
from datetime import datetime
from random import randint


def post_user_data(player:User):
    """create new player in database"""
    
    new_user = player.model_dump()
    
    for purchase in new_user['purchases']:
        if purchase['amount'] > 0:
            purchase['purchase_at'] = datetime.now()
            purchase['purchase_id'] = randint(100, 10000)
        else:
            purchase['purchase_at'] = datetime(1,1,1)
        
    users.insert_one(new_user)
    
    
    
    return {
        "message" : f"welcome {new_user['profile']['name']} {new_user['profile']['lastname']}",
    }
