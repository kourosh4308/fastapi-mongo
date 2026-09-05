from fastapi import status, HTTPException
from datetime import datetime

from models.purchases import Purchase
from models.users import Achivements
from db.purchase import create_purchase


def create_purchase_service(player_id:str,model:Purchase) -> Purchase:
    
    new_purchase = Purchase(
            purchase_token=model.purchase_token,
            amount=model.amount,
            items=model.items,
            purchase_at=datetime.now(),
            achivements=Achivements()
        )
    
    purchase : None | bool = create_purchase(player_id,new_purchase)
    
    if purchase is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user is not found')
    
    if purchase == False:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='purchase token is exist')
        
    return new_purchase
