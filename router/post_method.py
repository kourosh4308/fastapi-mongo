from fastapi import APIRouter, Request

from models.users_model import User, Purchase
from service.new_user import post_user_data_service
from service.new_purchase import create_purchase_service
from utils.limiter import limiter

router = APIRouter()

@router.post('/create-user', tags=['create user'])
@limiter.limit("3/minute")
def create_user(player:User,request:Request):
    
    return post_user_data_service(player)

@router.post('/new-purchase/{id}', tags=['new-purchase'])
@limiter.limit("3/minute")
def new_purchase(purchase:Purchase,player_id:str,request:Request):
    
    return create_purchase_service(player_id, purchase)
