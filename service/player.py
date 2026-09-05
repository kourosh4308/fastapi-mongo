from models.users import Player, User, Achivements, UpdatePlayer
from db.player import *

from fastapi import HTTPException, status
from typing import List, Any, Tuple, Optional
from uuid import uuid4
from datetime import datetime


def post_user_data_service(model:User) -> Player:
    new_player = Player(
        id=str(uuid4()),
        create_at=datetime.now(),
        profile=model.profile,
        achivements=Achivements(),
        stage=1
    )
    
    post_user_data(new_player)
    
    return new_player

def get_user_by_name_service(name:str) -> Player:
    player : Player = get_user_by_name(name)
    
    if player is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='player is not found')
    
    return player

def get_achivements_service(player_id:str) -> dict[str, int]:
    
    player : Tuple[Optional[Achivements], Optional[int]] = get_achivements(player_id)
    
    if player is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='player is not found')
    
    achivements, stage = player
    
    result = dict(achivements=achivements,
                  stage=stage)
    
    return result

def get_top_cups_service() -> List[dict[str, Any]]:
    players : List[dict[str, Any]] = get_top_cups()
    
    if players is None:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail='not player in this request')
    
    return players

def get_purchases_today_service() -> List[dict[str, Any]]:
    players : List[dict[str, Any]] = get_purchases_today()
    
    if players is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='no one player have purchase')
    
    return players

def get_all_players_service() -> List[Player]:
    
    players : List[Player] = get_all_players()
    
    if players is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='no one player')
    
    return players

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


def delete_user_service(name:str) -> bool:
    
    deleted_user = delete_user(name)
    
    if deleted_user == False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='user is not found')
    
    return True

