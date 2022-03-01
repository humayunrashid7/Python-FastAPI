from fastapi import Response, status, HTTPException, APIRouter, Depends
from app.db.schemas import UserResponse, CreateUserRequest, UpdateUserRequest
from app.db import models
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.utilities import utils

router = APIRouter(
    prefix='/api'
)

# GET: /api/users/5
@router.get('/users/{id}', response_model=UserResponse)
async def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'user with id: {id} not found!')
    return user

# POST: /api/users
@router.post('/users', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(user: CreateUserRequest, db: Session = Depends(get_db)):
    # hash the password
    hashed_password = utils.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user