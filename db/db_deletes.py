from mongo.db import users
from pymongo.results import DeleteResult


def delete_user(name:str) -> bool:
    """delete player by name"""
    
    deleted_user : DeleteResult = users.delete_one({'profile.name':name})
    
    if deleted_user.deleted_count == 0:
        return False
            
    return True
