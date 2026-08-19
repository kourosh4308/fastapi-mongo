from mongo.db import users
from datetime import datetime
from models.purchases_model import Purchase
from typing import Any


def create_purchase(id:str,purchase:Purchase) -> dict[str, str]:
    """add new purchase to database in user/purchase"""
    
    user = users.find_one({'id':id})
    
    if user is None:
        return{'message':'this id is not found'}
    
    token_exists = users.find_one({'id':id,'purchases.purchase_token':purchase.purchase_token})
    
    if token_exists:
        return {
            "message": "purchase already exists"
        }
    
    purchase_data : dict[str, Any] = purchase.model_dump()
    purchase_data['purchase_at'] = datetime.now()
    
    users.update_one({'id':id},{'$push':{'purchases':purchase_data}})
    
    return {'message':f"{user['profile']['name']} {user['profile']['lastname']} purchase is ok!"}    
