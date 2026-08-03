from fastapi import APIRouter
from models.users_model import User
from service.db.new_user import post_user_data
from mongo.db import users
from random import randint
from datetime import datetime


router = APIRouter()

@router.post('/create-user',tags=['create user'])
def create_user(player:User):
    
    return post_user_data(player)
