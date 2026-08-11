from fastapi import APIRouter, Request
from db.query_users import get_user_by_name, get_achivements, get_all_players
from db.query_users import  get_top_cups, get_purchases_today
from limiter.limiter import limiter


router = APIRouter(prefix='/player')

@router.get('/all',tags=['all player'])
@limiter.limit("5/minute")
def all_players(request:Request):
    all_users = get_all_players()
    
    if len(all_users) == 0 :
        return {'message' : 'no one login'}
    else :
        return all_users

@router.get('/{cups}/top-cup-users',tags=['top cups'])
@limiter.limit("5/minute")
def top_users(request:Request):
     
    all_users = get_top_cups()
    
    if len(all_users) == 0:
        return {'message':'nobody have top cups'}
    else:
        return all_users

@router.get('/{gems}/show-achivements',tags=['show achivements'])
@limiter.limit("5/minute")
def show_achivements(name:str,request:Request):
    
    return get_achivements(name)

@router.get('/purchases',tags=['purchase now'])
@limiter.limit("5/minute")
def player_purchase(request:Request):
    all_users = get_purchases_today()
  
    if len(all_users) == 0:
        return {'message':'nobody have purchase'}
    else:
        return all_users

@router.get('search-name/{name}',tags=['search player by name'])
@limiter.limit("5/minute")
def player(name:str,request:Request):
    
    return get_user_by_name(name)
    