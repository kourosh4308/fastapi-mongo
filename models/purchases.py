from pydantic import BaseModel, Field
from typing import List
from datetime import datetime


class Purchase(BaseModel):
    purchase_token :str
    amount : int
    items : List[str] = Field(default_factory=list)
    purchase_at : datetime = Field(default_factory=datetime.now)
