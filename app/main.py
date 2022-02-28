from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.app_v1.routers import posts

# Declare App
app = FastAPI()

# Config CORS
app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

#Config Routing
app.include_router(posts.router)

# API Root Method
@app.get('/')
async def root():
    return {'message': 'Hello World!'}