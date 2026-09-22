from fastapi import HTTPException, status

from db.friend import friend_ship
from models.friend import FriendShip


def friend_ship_service(model:FriendShip) -> FriendShip | dict[str,str]:
    
    result = friend_ship(model)
    
    if result == -1:
        return {'message':'friend id not found'}
    
    if result == -2:
        return {'message' : 'player id not found'}
    
    return result
