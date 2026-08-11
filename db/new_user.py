from models.users_model import CreateUser
from mongo.db import users
from typing import Any
from datetime import datetime
from uuid import uuid4


def post_user_data(player:CreateUser) -> dict[str, str]:
    """create new player in database"""
    
    new_user : dict[str, Any] = player.model_dump(mode='json')
    
    new_user_id = str(uuid4())
    
    new_user["_id"] = new_user_id
    
    new_user['create_at'] = datetime.now()
    
    users.insert_one(new_user)
    
    return {
        "id": new_user['_id'],
        "message" : f"welcome {new_user['profile']['name']} {new_user['profile']['lastname']}",
    }
