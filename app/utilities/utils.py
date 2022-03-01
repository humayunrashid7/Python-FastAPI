from passlib.context import CryptContext

# Choose hashing algorithm: 'bcrypt' in this case
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash(password: str):
    # return the hashed password
    return pwd_context.hash(password)