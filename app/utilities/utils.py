from passlib.context import CryptContext

# Choose hashing algorithm: 'bcrypt' in this case
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    # return the hashed password
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)