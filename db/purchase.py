from mongo.db import users
from models.purchases import Purchase


def create_purchase(player_id:str,purchase:Purchase) -> None | bool:
    """add new purchase to database in user/purchase"""
    
    user : bool | None = users.find_one({'id':player_id})
    
    if user is None:
        return None
    
    token_exists = users.find_one({'id':player_id,'purchases.purchase_token':purchase.purchase_token})
    
    if token_exists:
        return False
    
    users.update_one({'id':player_id},{'$push':{'purchases':purchase.model_dump()}})
    
    return True
