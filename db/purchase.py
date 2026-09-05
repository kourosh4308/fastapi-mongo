from typing import List, Any
from datetime import datetime, timedelta
from pymongo.cursor import Cursor

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

def get_purchases_today() -> List[dict[str, Any]] | None:
    """get name and lastnames of players who had purchases"""
    
    today : datetime = datetime.now()
    
    start : datetime = today.replace(hour=0,minute=0,second=0,microsecond=0)
    end : datetime = start + timedelta(days=1)
    
    cursor : Cursor = (
        users.find({'purchases.purchase_at':{'$gt':start,'$lt':end}},
                   {
                       '_id':0,
                       'id':1,
                       'profile.name':1,
                       'profile.lastname':1,
                       'purchases':1
                    })
    )
    
    result : List[dict[str, Any]] = list((purchse)for purchse in cursor)
    
    if len(result) == 0:
        return None
    
    return result
