from fastapi import APIRouter, Request
from service.db_deletes import delete_user_service
from utils.limiter import limiter


router = APIRouter(prefix='/delete')

@router.delete('/delete/{name}',tags=['delete player'])
@limiter.limit("5/minute")
def delete_player(name:str,request:Request) -> bool:
    
    return delete_user_service(name)
