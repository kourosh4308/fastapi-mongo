from fastapi import APIRouter
from mongo.db import users


router = APIRouter(prefix='/delete')

@router.delete('/{name}/delete',tags=['delete player'])
def delete_player(name:str):
    user = users.find_one({'profile.name':name})
    
    users.delete_one(user)
    
    return {'message':'deleted user successful'}
