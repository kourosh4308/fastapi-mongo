from models.friend import FriendShip
from mongo.db import users


def friend_ship(model:FriendShip) -> int:
    friend = users.find_one({"id":model.friend_id})
    
    if friend is None:
        return -1
    
    player = users.find_one({'id':model.player_id})
    
    if player is None:
        return -2
    
    users.update_one(
        {'id':model.player_id},
        {'$push':{'friendship':model.model_dump(mode="json")}}
        )
    
    return 1
