from fastapi import APIRouter
from models.users_model import User
from mongo.db import users
from random import randint
from datetime import datetime


router = APIRouter()

@router.post('/create-user',tags=['create user'])
def create_user(player:User):
    user = player.model_dump()
    
    for purchase in user['purchases']:
        
        if purchase['amount'] > 0:
            purchase['purchase_id'] = randint(100, 10000)
            purchase['purchase_at'] = datetime.now()
        else:
            purchase['purchase_id'] = 0
            purchase['purchase_at'] = datetime(1,1,1)

    users.insert_one(user)
    
    return {
        'message' : 'create playes successful',
        'name' : f"{user['profile']['name']} {user['profile']['lastname']}"
    }
    
