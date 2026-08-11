from pydantic import BaseModel, Field
from typing import List


class Purchase(BaseModel):
    purchase_token :str
    amount : int
    items : List[str] = Field(default_factory=list)
