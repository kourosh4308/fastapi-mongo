from db.db_deletes import delete_user
from fastapi import HTTPException, status


def delete_user_service(name:str) -> bool:
    
    deleted_user = delete_user(name)
    
    if deleted_user == False:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='user is not found')
    
    return True
