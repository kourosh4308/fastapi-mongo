from models.users_model import User
from mongo.db import users


def post_user_data(player:User) -> None:
    """create new player in database"""
    
    users.insert_one(player.model_dump())
    