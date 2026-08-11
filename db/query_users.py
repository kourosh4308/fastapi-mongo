from mongo.db import users
from datetime import datetime,timedelta
from typing import List, Any
from pymongo.cursor import Cursor
from models.users_model import User, TopCupPlayer, User_has_Purchase
from convert.convert_data import convert_id, convert_topplayer_id, convert_user_has_purchase_id


def get_top_cups() -> List[TopCupPlayer]:
    """get 10 tops players from db"""
    
    cursor : Cursor = (
        users.find(
            {'achivements.cups':{'$gt':10000}},
            {
                'profile.name':1,
                'profile.lastname':1,
                'achivements':1
            }
        )
        .sort('achivements.cups',-1)
        .limit(10)
    )
    
    return [
        convert_topplayer_id(user)for user in cursor
    ]
    
def get_all_players() -> List[User]:
    """get list of all players"""
    
    cursor : Cursor = (
        users.find()
    )
    
    return [
        convert_id(user)for user in cursor
    ]
    
def get_achivements(name:str) -> dict[str, Any]:
    """get achivements with filter by name"""
    
    user : dict[str, Any] = users.find_one(
            {'profile.name':name},
            {
                'achivements':1,
                'profile.name':1,
                'profile.lastname':1
            }
        )
    
    return convert_topplayer_id(user)

def get_purchases_today() -> list[User_has_Purchase]:
    """get name and lastnames of players who had purchases"""
    
    today : datetime = datetime.now()
    
    start : datetime = today.replace(hour=0,minute=0,second=0,microsecond=0)
    end : datetime = start + timedelta(days=1)
    
    cursor : Cursor = (
        users.find({'purchases.purchase_at':{'$gt':start,'$lt':end}},
                   {
                       'profile.name':1,
                       'profile.lastname':1,
                       'purchases':1
                    })
    )
    
    return [
        convert_user_has_purchase_id(user)for user in cursor
    ]

def get_user_by_name(name:str) -> User:
    """search player by name"""
    
    user : dict[str, Any] = users.find_one({'profile.name':name})
    
    if user is None:
        return {"message":f"{name} is not found"}
    else:
        
        return convert_id(user)
