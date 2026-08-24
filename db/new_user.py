from models.users_model import User
from mongo.db import users
from typing import Any
from datetime import datetime
from uuid import uuid4
from utils.remove_id import exclude_keys
from models.users_model import Achivements


def post_user_data(player:User) -> dict[str, str]:
    """create new player in database"""
    
    new_user : dict[str, Any] = player.model_dump()
        
    new_user["id"] = str(uuid4())
    
    new_user['create_at'] = datetime.now()
    
    new_user['achivements'] = Achivements().model_dump()
    
    new_user['stage'] = 1
    
    users.insert_one(new_user)
    
    new_user = exclude_keys(new_user, ["_id"])
    
    return {
        "id": new_user['id'],
        "message" : f"welcome {new_user['profile']['name']} {new_user['profile']['lastname']}",
    }
