from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.app_v1.routers import posts
from app.app_v1.routers import users
from app.app_v1.routers import auth

# Declare App
app = FastAPI(title="FastAPI CRUD", version="1.0.0")

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
app.include_router(users.router)
app.include_router(auth.router)

# API Root Method
@app.get('/')
async def root():
    return {'message': 'Hello World!'}