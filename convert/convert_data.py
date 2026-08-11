from models.users_model import User, TopCupPlayer, User_has_Purchase
from typing import Any


def convert_id(user:dict) -> User:
    user['id'] = user.pop('_id')
    
    return User.model_validate(user)

def convert_topplayer_id(user:dict) -> TopCupPlayer:
    user['id'] = user.pop('_id')
    user['name'] = user['profile']['name']
    user['lastname'] = user['profile']['lastname']
    user['achivements'] = user['achivements']
    
    return TopCupPlayer.model_validate(user)

def convert_user_has_purchase_id(user:dict[str,Any]) -> User_has_Purchase:
    user['id'] = user.pop('_id')
    user['name'] = user['profile']['name']
    user['lastname'] = user['profile']['lastname']
    user['purchases'] = user['purchases']
    
    return User_has_Purchase.model_validate(user)
