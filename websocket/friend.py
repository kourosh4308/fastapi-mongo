from fastapi import WebSocket, WebSocketDisconnect
from typing import List

from service.friend import friend_ship_service
from models.friend import FriendShip


players : List[WebSocket] = []

async def friendship(websocket:WebSocket):
    await websocket.accept()
    
    players.append(websocket)
    
    print('connected!!!')
    
    try:
        while True:
            data = await websocket.receive_json()
            
            friendship_data = FriendShip(**data)
            
            friend_ship_service(friendship_data)
            
            print('received', data)
            
            await websocket.send_json({'message':'friend request sent', 'data':friendship_data.model_dump(mode="json")})
            
    except WebSocketDisconnect:
        if websocket in players:
            players.remove(websocket)
            
        print('player disconnected')
