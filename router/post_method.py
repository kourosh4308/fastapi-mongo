from fastapi import APIRouter, Request

from models.users import User
from models.purchases import Purchase
from service.player import post_user_data_service
from service.purchase import create_purchase_service
from utils.limiter import limiter

router = APIRouter()

@router.post('/create-user', tags=['create user'])
@limiter.limit("3/minute")
def create_user(player:User,request:Request):
    
    return post_user_data_service(player)

@router.post('/new-purchase/{player_id}', tags=['new-purchase'])
@limiter.limit("3/minute")
def new_purchase(purchase:Purchase,player_id:str,request:Request):
    
    return create_purchase_service(player_id, purchase)
