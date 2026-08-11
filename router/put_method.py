from fastapi import APIRouter, Request
from limiter.limiter import limiter
from db.new_purchase import create_purchase
from models.purchases_model import Purchase



router = APIRouter()

@router.put('/new-purchase/{id}',tags=['new purchase'])
@limiter.limit("3/minute")
def new_purchase(purchase:Purchase,id:str,request:Request):
    
    return create_purchase(id,purchase)

