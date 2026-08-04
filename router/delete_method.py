from fastapi import APIRouter
from service.db.query_users import delete_user


router = APIRouter(prefix='/delete')

@router.delete('/{name}/delete',tags=['delete player'])
def delete_player(name:str):
    
    return delete_user(name)
