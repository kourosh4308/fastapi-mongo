from fastapi import APIRouter, Request

from utils.limiter import limiter
from service.update_player import put_update_player_service
from models.users_model import UpdatePlayer


router = APIRouter()

@router.put('/update-user/{id}',tags=['update-user'])
@limiter.limit("3/minute")
def update_player(model:UpdatePlayer,id:str,request:Request):
    
    return put_update_player_service(id,model)
