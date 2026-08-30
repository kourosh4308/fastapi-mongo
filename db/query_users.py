from mongo.db import users
from datetime import datetime,timedelta
from typing import List, Any, Tuple, Optional
from pymongo.cursor import Cursor
from models.users_model import Player, Achivements
from utils.remove_id import __model_player_from_document


def get_top_cups() -> List[dict[str, Any]] | None:
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
    
    players : List[dict[str, Any]] = list((player)for player in cursor)
    
    if len(players) == 0:
        return None
    
    return players
    
def get_all_players() -> List[Player] | None:
    """get list of all players"""
    
    cursor : Cursor = users.find()
    
    players : List[Player] = list(map(__model_player_from_document, cursor))
    
    if len(players) == 0:
        return None
    
    return players
    
def get_achivements(player_id:str) -> Tuple[Optional[Achivements], Optional[int]] | None:
    """get achivements with filter by name"""
    
    user : dict[str, Any] = users.find_one(
            {'id':player_id},
            {
                '_id':0,
                'achivements':1,
                'stage':1
            }
        )
    
    if user is None:
        return None
    
    achivements = user.get('achivements')
    stage = user.get('stage')
    
    return (achivements, stage)

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

def get_user_by_name(name:str) -> Player | None:
    """search player by name"""
    
    user : dict[str, Any] = users.find_one({'profile.name':name})
    
    if user is None:
        return None
    
    user = __model_player_from_document(user)
        
    return user
