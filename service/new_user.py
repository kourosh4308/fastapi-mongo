from db.new_user import post_user_data
from models.users_model import Player, User, Achivements

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
