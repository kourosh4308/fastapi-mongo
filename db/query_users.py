from mongo.db import users
from datetime import datetime,timedelta
from typing import List, Any
from pymongo.cursor import Cursor
from models.users_model import Player
from utils.remove_id import exclude_keys, __model_player_from_document


def get_top_cups() -> List[dict[str, Any]]:
    """get 10 tops players from db"""
    
    cursor : Cursor = (
        users.find(
            {'achivements.cups':{'$gt':10000}},
            {
                '_id':0,
                'id':1,
                'profile.name':1,
                'profile.lastname':1,
                'achivements':1
            }
        )
        .sort('achivements.cups',-1)
        .limit(10)
    )
    
    return [
        (player)for player in cursor
    ]
    
def get_all_players() -> List[Player]:
    """get list of all players"""
    
    cursor : Cursor = users.find()
    
    players : List[Player] = list(map(__model_player_from_document, cursor))
    
    return players
    
def get_achivements(name:str) -> dict[str, Any]:
    """get achivements with filter by name"""
    
    user : dict[str, Any] = users.find_one(
            {'profile.name':name},
            {
                '_id':0,
                'id':1,
                'achivements':1,
                'profile.name':1,
                'profile.lastname':1
            }
        )
    
    return user

def get_purchases_today() -> list[dict[str, Any]]:
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
    
    return [
        (user)for user in cursor
    ]

def get_user_by_name(name:str) -> Player:
    """search player by name"""
    
    user : dict[str, Any] = users.find_one({'profile.name':name})
    
    if user is None:
        return {"message":f"{name} is not found"}
    else:
        
        user = exclude_keys(user, ["_id"])
        
        return user
