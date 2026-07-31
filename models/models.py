from pydantic import BaseModel
from datetime import datetime


class Profile(BaseModel):
    name : str
    lastname : str
    email : str
    sex : str
    phone_nubmer : str
    
class Archivements(BaseModel):
    golds : int = 1000
    gems : int = 100
    cups : int = 0
    
class Purchases(BaseModel):
    purchase_id : int = 0
    amount : int
    item : list[str]
    purchase_at : datetime
    
class User(BaseModel):
    create_at : datetime
    profile : Profile
    archivements : Archivements
    purchases : list[Purchases]
    stage : int = 1
