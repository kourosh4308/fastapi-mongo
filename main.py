from fastapi import FastAPI
from router import post_method, get_method, delete_method, put_method


app = FastAPI()
app.include_router(post_method.router)
app.include_router(get_method.router)
app.include_router(delete_method.router)
app.include_router(put_method.router)
