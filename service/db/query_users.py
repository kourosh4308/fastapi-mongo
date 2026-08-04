from mongo.db import users
from datetime import datetime,timedelta


def get_top_cups():
    """get 10 tops players from db"""
    
    cursor = (
        users.find(
            {'achivements.cups':{'$gt':10000}},
            {
                'profile.name':1,
                'achivements.cups':1
            }
        )
        .sort('achivements.cups',-1)
        .limit(10)
    )
    
    return [
        {**user, "_id" : str(user["_id"])}
        for user in cursor
    ]
    
def get_all_players():
    """get list of all players"""
    
    cursor = (
        users.find()
    )
    
    return [
        {**user, "_id" : str(user["_id"])}for user in cursor
    ]
    
def get_gems(name:str = None):
    """get gems with filter by name"""
    
    user = users.find_one(
            {'profile.name':name},
            {'achivements.gems':1}
        )
    
    user["_id"] = str(user["_id"])
    
    return user

def get_purchases_today():
    """get name and lastnames of players who had purchases"""
    
    today = datetime.now()
    
    start = today.replace(hour=0,minute=0,second=0,microsecond=0)
    end = start + timedelta(days=1)
    
    cursor = (
        users.find({'purchases.purchase_at':{'$gt':start,'$lt':end}},{'profile.name':1,'profile.lastname':1})
    )
    
    return [
        {**user, "_id": str(user["_id"])}for user in cursor
    ]

def get_user_by_name(name:str):
    """search player by name"""
    
    user = users.find_one({'profile.name':name})
    
    if user is None:
        return {"message":f"{name} is not found"}
    else:
        user["_id"] = str(user["_id"])
        return user

def delete_user(name:str):
    """delete player by name"""
    
    deleted_user = users.delete_one({'profile.name':name})
    
    if deleted_user.deleted_count == 0:
        return {"message":f"{name} is not found"}
            
    return {"message":f"{name} is deleted"}
