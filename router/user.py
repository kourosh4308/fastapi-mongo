from fastapi import APIRouter, Request

from models.users import User, UpdatePlayer
from service.player import delete_user_service, post_user_data_service, put_update_player_service
from service.player import get_user_by_name_service, get_all_players_service
from utils.limiter import limiter


router = APIRouter()

@router.post('/create-user', tags=['create user'])
@limiter.limit("3/minute")
def create_user(player:User,request:Request):
    
    return post_user_data_service(player)

@router.put('/update-player/{id}',tags=['update-user'])
@limiter.limit("3/minute")
def update_player(model:UpdatePlayer,id:str,request:Request):
    
    return put_update_player_service(id,model)

@router.get('/all-players',tags=['all player'])
@limiter.limit("5/minute")
def all_players(request:Request):
    
    return get_all_players_service()

@router.get('/search-player-by-name/{name}',tags=['search player by name'])
@limiter.limit("5/minute")
def player(name:str,request:Request):
    
    return get_user_by_name_service(name)

@router.delete('/delete-player/{name}',tags=['delete player'])
@limiter.limit("5/minute")
def delete_player(name:str,request:Request) -> bool:
    
    return delete_user_service(name)
