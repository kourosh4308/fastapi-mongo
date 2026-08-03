from pydantic import BaseModel
from datetime import datetime


class Purchase(BaseModel):
    purchase_id : int = 0
    amount : int
    items : list[str]
    purchase_at : datetime
