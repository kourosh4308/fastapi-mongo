from fastapi import APIRouter, Request
from models.users_model import CreateUser
from models.purchases_model import Purchase
from db.new_user import post_user_data
from db.new_purchase import create_purchase
from limiter.limiter import limiter


router = APIRouter()

@router.post('/create-user',tags=['create user'])
@limiter.limit("3/minute")
def create_user(player:CreateUser,request:Request):
    
    return post_user_data(player)
