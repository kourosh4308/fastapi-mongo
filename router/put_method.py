from fastapi import APIRouter, Request
from db.new_purchase import create_purchase
from models.purchases_model import Purchase
from slowapi import Limiter
from slowapi.util import get_remote_address


limiter = Limiter(key_func=get_remote_address)

router = APIRouter()

@router.put('/new-purchase/{id}',tags=['new purchase'])
@limiter.limit("3/minute")
def new_purchase(purchase:Purchase,id:str,request:Request):
    
    return create_purchase(id,purchase)

