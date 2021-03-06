from typing import Optional
from pydantic import BaseModel, EmailStr
from datetime import datetime

class CreatePostRequest(BaseModel):
    title: str
    content: str
    published: bool = True
    created_at: datetime = datetime.now()

class UpdatePostRequest(BaseModel):
    title: str
    content: str
    published: bool = True

class UserResponse(BaseModel):
    id: int
    email: str
    password: str
    created_at: datetime
    class Config:
        orm_mode = True
class Post(BaseModel):
    id: int
    title: str
    content: str
    published: bool
    created_at: datetime
    user_id: int
    user: UserResponse
    class Config:
        orm_mode = True

class PostResponse(BaseModel):
    Post: Post
    votes: int
class CreateUserRequest(BaseModel):
    email: EmailStr
    password: str
    created_at: datetime = datetime.now()

class UpdateUserRequest(BaseModel):
    email: str
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class CreateVoteRequest(BaseModel):
    post_id: int
    dir: int # 0: remove vote/like, 1: add vote/like