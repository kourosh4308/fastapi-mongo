from mongo.db import users
from pymongo.results import DeleteResult


def delete_user(name:str) -> dict[str, str]:
    """delete player by name"""
    
    deleted_user : DeleteResult = users.delete_one({'profile.name':name})
    
    if deleted_user.deleted_count == 0:
        return {"message":f"{name} is not found"}
            
    return {"message":f"{name} is deleted"}
