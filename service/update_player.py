from fastapi import HTTPException, status

from models.users_model import UpdatePlayer
from db.update_player import put_update_player


def put_update_player_service(player_id:str,model:UpdatePlayer) -> int:
    
    data : dict[str, int] = model.model_dump(exclude_unset=True)
    
    achive_fields = {'gems','golds','cups'}
    
    set_update = {}

    for key, value in data.items():
        if key in achive_fields:
            set_update[f"achivements.{key}"] = value
        else:
            set_update[key] = value

    matched_count, modified_count = put_update_player(player_id,set_update)
    
    if matched_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user is not found')
    
    return modified_count
