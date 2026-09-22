from fastapi import APIRouter, WebSocket

from websocket.friend import friendship


router = APIRouter()

@router.websocket('/ws/friends')
async def friendship_websocket(websocket:WebSocket):
    
    await friendship(websocket)
    
    
