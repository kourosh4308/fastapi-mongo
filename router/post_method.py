from fastapi import APIRouter
from models.models import User
from mongo.db import users
from random import randint


router = APIRouter()

@router.post('/create-user',tags=['create user'])
def create_user(player:User):
    user = player.model_dump()
    
    for purchase in user['purchases']:
        if purchase['amount'] > 0:
            purchase['purchase_id'] = randint(100, 10000)
        else:
            purchase["purchase_id"] = 0
            
    users.insert_one(user)
    
    return {
        'message' : 'create playes successful',
        'name' : f"{user['profile']['name']} {user['profile']['lastname']}"
    }
    
