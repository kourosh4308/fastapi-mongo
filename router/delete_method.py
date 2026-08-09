from fastapi import APIRouter, Request
from service.db.query_users import delete_user
from service.limiter.limiter import limiter


router = APIRouter(prefix='/delete')

@router.delete('/delete/{name}',tags=['delete player'])
@limiter.limit("5/minute")
def delete_player(name:str,request:Request):
    
    return delete_user(name)
