from fastapi import APIRouter, Request

from service.player import *
from utils.limiter import limiter


router = APIRouter(prefix='/player')

@router.get('/all',tags=['all player'])
@limiter.limit("5/minute")
def all_players(request:Request):
    
    return get_all_players_service()

@router.get('/top-cup-users',tags=['top cups'])
@limiter.limit("5/minute")
def top_users(request:Request):
     
    return get_top_cups_service()
    
@router.get('/show-achivements',tags=['show achivements'])
@limiter.limit("5/minute")
def show_achivements(player_id:str,request:Request):
    
    return get_achivements_service(player_id)

@router.get('/purchases',tags=['purchase now'])
@limiter.limit("5/minute")
def player_purchase(request:Request):
    
    return get_purchases_today_service()

@router.get('/search-name/{name}',tags=['search player by name'])
@limiter.limit("5/minute")
def player(name:str,request:Request):
    
    return get_user_by_name_service(name)
