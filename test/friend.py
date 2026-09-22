from fastapi.testclient import TestClient

from main import app


client = TestClient(app)


def test_friendship():

    with client.websocket_connect("/ws/friends") as websocket:

        websocket.send_json({
            "player_id": "484e3017-2878-467a-81d7-c33b39192b0e",
            "friend_id": "fef38137-0a7c-48db-98a7-e1fa36e1bae1"
        })

        response = websocket.receive_json()

        assert response["message"] == "friend request sent"

        assert response["data"]["player_id"] == "484e3017-2878-467a-81d7-c33b39192b0e"
        assert response["data"]["friend_id"] == "fef38137-0a7c-48db-98a7-e1fa36e1bae1"
        assert response["data"]["status"] == "in pending"
