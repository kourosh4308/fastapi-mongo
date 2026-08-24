from mongo.db import users
from models.users_model import UpdatePlayer
from fastapi import status, HTTPException
from uuid import UUID


def put_update_player(id:str,model:UpdatePlayer) -> dict:
    player =  users.find_one({'id':id})
    
    if player is None:
        raise HTTPException (status_code=status.HTTP_404_NOT_FOUND,detail='player not found')
    
    data : dict[str, int] = model.model_dump(exclude_unset=True)
    
    achive_fields = {'gems','golds','cups'}
    
    set_update = {}
    
    for key, value in data.items():
        if key in achive_fields:
            set_update[f"achivements.{key}"] = value
        else:
            set_update[key] = value
        
    users.update_one({'id':id},{'$set':set_update})
    
    return {'message':'updated is ok'}
