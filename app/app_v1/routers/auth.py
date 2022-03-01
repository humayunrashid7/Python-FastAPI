from os import access
from fastapi import Response, status, HTTPException, APIRouter, Depends
from app.db.database import get_db
from app.db import models
from sqlalchemy.orm import Session
from app.db.schemas import LoginRequest, TokenResponse
from app.utilities import utils
from app.auth import oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    prefix='/api'
)

# POST: /api/login
@router.post('/login', response_model=TokenResponse)
async def create_user(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()

    if not user or not utils.verify_password(request.password, user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                            detail=f'Invalid Credentials')

    # Create a Token
    access_token = oauth2.create_access_token(data= {'user_id': user.id})

    # Return Token
    return {"access_token": access_token, 'token_type': 'bearer'}