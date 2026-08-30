from db.query_users import get_user_by_name, get_achivements,get_top_cups, get_all_players, get_purchases_today
from models.users_model import Player, Achivements
from fastapi import HTTPException, status
from typing import List, Any, Tuple, Optional


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
