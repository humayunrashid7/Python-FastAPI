from fastapi import FastAPI
from app.app_v1.routers import posts

app = FastAPI()

app.include_router(posts.router)

@app.get('/')
async def root():
    return {'message': 'Hello World!'}