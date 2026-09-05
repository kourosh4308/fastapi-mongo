from fastapi import APIRouter, Request

from service.player import get_top_cups_service, get_achivements_service
from utils.limiter import limiter


router = APIRouter(prefix='/top-players')

@router.get('/top-cup-players',tags=['top cups'])
@limiter.limit("5/minute")
def top_users(request:Request):
     
    return get_top_cups_service()
    
@router.get('/show-achivements',tags=['show achivements'])
@limiter.limit("5/minute")
def show_achivements(player_id:str,request:Request):
    
    return get_achivements_service(player_id)
