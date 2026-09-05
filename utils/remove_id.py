from models.users import Player
from typing import Any


def exclude_keys(doc: dict[str, Any], keys: list[str]) -> dict[str, Any]:
    """If the key we gave it was deleted, it will return a new dictionary"""
    return {key: value for key, value in doc.items() if key not in keys}

def __model_player_from_document(player_doc:dict[str, Any]) -> Player:
    """The item we specified should be deleted"""
    return Player.model_validate(exclude_keys(player_doc, ["_id"]))
