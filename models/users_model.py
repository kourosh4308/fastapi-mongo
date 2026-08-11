from pydantic import BaseModel, Field
from datetime import datetime
from models.purchases_model import Purchase
from uuid import UUID, uuid4
from typing import List


class Profile(BaseModel):
    name : str
    lastname : str
    email : str
    sex : str
    phone_number : str
    
class Achivements(BaseModel):
    golds : int = 1000
    gems : int = 100
    cups : int = 0
    
class CreateId(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    
class CreateUser(BaseModel):
    profile : Profile
    achivements : Achivements
    stage : int = 1
    
class User(BaseModel):
    id : UUID 
    create_at : datetime
    profile : Profile
    achivements : Achivements
    purchases : List[Purchase] = Field(default_factory=list)
    stage : int

class TopCupPlayer(BaseModel):
    id : UUID
    name : str
    lastname : str
    achivements : Achivements
    
class User_has_Purchase(BaseModel):
    id : UUID
    name : str
    lastname : str
    purchases : List[Purchase]
