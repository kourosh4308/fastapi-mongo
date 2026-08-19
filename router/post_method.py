from fastapi import APIRouter, Request
from models.users_model import User
from db.new_user import post_user_data
from slowapi import Limiter
from slowapi.util import get_remote_address


limiter = Limiter(key_func=get_remote_address)

router = APIRouter()

@router.post('/create-user',tags=['create user'])
@limiter.limit("3/minute")
def create_user(player:User,request:Request):
    
    return post_user_data(player)
