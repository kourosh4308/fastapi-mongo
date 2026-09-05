from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

from models.purchases import Purchase


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
    
class Player(BaseModel):
    id : str 
    create_at : Optional[datetime] = None
    profile : Optional[Profile] = None
    achivements : Optional[Achivements] = None
    purchases : Optional[List[Purchase]] = Field(default_factory=list)
    stage : Optional[int] = 1
    
class UpdatePlayer(BaseModel):
    golds : Optional[int] = None
    gems : Optional[int] = None
    cups : Optional[int] = None
    stage : Optional[int] = None
