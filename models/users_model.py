from pydantic import BaseModel, Field
from datetime import datetime
from models.purchases_model import Purchase
from uuid import UUID, uuid4
from typing import List, Optional


class Profile(BaseModel):
    name : str
    lastname : str
    email : Optional[str] = None
    sex : Optional[str] = None
    phone_number : Optional[str] = None
    
class Achivements(BaseModel):
    golds : int = 1000
    gems : int = 100
    cups : int = 0

class User(BaseModel):
    profile : Profile
    achivements : Achivements
    stage : int = 1
    
class Player(BaseModel):
    id : UUID 
    create_at : Optional[datetime] = None
    profile : Optional[Profile] = None
    achivements : Optional[Achivements] = None
    purchases : Optional[List[Purchase]] = Field(default_factory=list)
    stage : Optional[int] = None
