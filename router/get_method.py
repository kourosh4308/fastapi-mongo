from fastapi import APIRouter
from mongo.db import users
from datetime import datetime


router = APIRouter(prefix='/player')

@router.get('/all',tags=['all player'])
def all_players():
    all_users = []
    
    for player in users.find():
        
        player['_id'] = str(player['_id'])
        
        all_users.append(player)
        
    return all_users

@router.get('/{cups}/top-cups',tags=['top cups'])
def top_cups():
    
    all_users = []
    for user in users.find({'archivements.cups':{'$gt':10000}}).sort('archivements.cups',-1).limit(10):
        user['_id'] = str(user['_id'])
        
        all_users.append(user)

    if len(all_users) == 0:
        return {'message':'nobody have top cups'}
    else:
        return all_users

@router.get('/{gems}/show-gems',tags=['show gems'])
def show_gems(name:str):
    user = users.find_one({'profile.name':name},{'archivements.gems':1})
    
    user['_id'] = str(user['_id'])
    
    return user

@router.get('/purchases',tags=['purchase now'])
def player_purchase():
    all_users = []
    
    today = datetime.now().date()
    
    for user in users.find():
        print(type(user))
        for purchase in user['purchases']:
            if purchase['purchase_at'].date() == today:
                
                user['_id'] = str(user['_id'])
        
                all_users.append(user)
                break
        
    if len(all_users) == 0:
        return {'message':'nobody have purchase'}
    else:
        return all_users

@router.get('/{name}',tags=['search player by name'])
def player(name:str):
    user = users.find_one({'profile.name':name})

    if user is None:
        return {'message':'user not found'}

    user['_id'] = str(user['_id'])
    
    return user
