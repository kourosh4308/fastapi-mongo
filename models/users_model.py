from pydantic import BaseModel
from datetime import datetime
from models.purchases_model import Purchase


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
    
class User(BaseModel):
    create_at : datetime
    profile : Profile
    achivements : Achivements
    purchases : list[Purchase]
    stage : int = 1
