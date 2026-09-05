from fastapi import FastAPI
from router import leaderboard, purchase, user


app = FastAPI()
app.include_router(leaderboard.router)
app.include_router(purchase.router)
app.include_router(user.router)
