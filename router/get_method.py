from fastapi import APIRouter
from service.db.query_users import get_user_by_name, get_gems, get_all_players
from service.db.query_users import  get_top_cups, get_purchases_today


router = APIRouter(prefix='/player')

@router.get('/all',tags=['all player'])
def all_players():
    all_users = get_all_players()

    if len(all_users) == 0 :
        return {'message' : 'no one login'}
    else :
        return all_users

@router.get('/{cups}/top-cup-users',tags=['top cups'])
def top_users():
     
    all_users = get_top_cups()
    if len(all_users) == 0:
        return {'message':'nobody have top cups'}
    else:
        return all_users

@router.get('/{gems}/show-gems',tags=['show gems'])
def show_gems(name:str):
    
    return get_gems(name)

@router.get('/purchases',tags=['purchase now'])
def player_purchase():
    all_users = get_purchases_today()
  
    if len(all_users) == 0:
        return {'message':'nobody have purchase'}
    else:
        return all_users

@router.get('/{name}',tags=['search player by name'])
def player(name:str):
    
    return get_user_by_name(name)
    