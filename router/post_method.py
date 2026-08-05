from fastapi import APIRouter, Request
from models.users_model import User
from service.db.new_user import post_user_data
from service.limiter.limiter import limiter


router = APIRouter()

@router.post('/create-user',tags=['create user'])
@limiter.limit("3/minute")
def create_user(player:User,request:Request):
    
    return post_user_data(player)
