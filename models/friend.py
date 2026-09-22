from pydantic import BaseModel, Field
from datetime import datetime


class FriendShip(BaseModel):
    player_id : str
    friend_id : str
    create_at : datetime = Field(default_factory=datetime.now)
    status : str = "in pending"
