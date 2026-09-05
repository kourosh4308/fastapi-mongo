from fastapi import APIRouter, Request

from utils.limiter import limiter
from models.purchases import Purchase
from service.purchase import create_purchase_service, get_purchases_today_service


router = APIRouter(prefix='/purchase')

@router.post('/new-purchase/{player_id}', tags=['new-purchase'])
@limiter.limit("3/minute")
def new_purchase(purchase:Purchase,player_id:str,request:Request):
    
    return create_purchase_service(player_id, purchase)

@router.get('/purchases',tags=['purchase today'])
@limiter.limit("5/minute")
def player_purchase(request:Request):
    
    return get_purchases_today_service()

