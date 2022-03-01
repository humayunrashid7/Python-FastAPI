from jose import JWTError, jwt
from datetime import datetime, timedelta
from app.db.schemas import TokenResponse, TokenData
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from app.db.database import get_db
from sqlalchemy.orm import Session
from app.db import models

# Token URL is path of Http Post method to login
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='api/login')

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    # Create copy of data needed to encode
    to_encode = data.copy()

    # Calculate the expiry time of token & attach to data
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    
    # Create the token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def verify_access_token(token: str, login_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get('user_id')

        if user_id is None:
            raise login_exception
        
        token_data = TokenData(id=user_id)
    except JWTError:
        raise login_exception
    
    return token_data

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    login_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='could not validate credentials',
                            headers={'WWW-Authenticate': 'Bearer'})
    
    token = verify_access_token(token, login_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    return user
