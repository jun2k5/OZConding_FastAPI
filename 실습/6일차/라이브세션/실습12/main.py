from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer

from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta


from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from sqlalchemy import select
from model import User

app = FastAPI()

############################
# utils
############################

#password

pwd_context = CryptContext(
    schemes= ["argon2"],
    deprecated="auto"
)

def hash_password(password: str):
    return pwd_context.hash(password)

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)





# jwt
ALGORITHM = "HS256"
SECRET_KEY = "be16-oz" #자물쇠
ACCESS_TOKEN_EXPIRE_MINS = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINS)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


# OAuth2 Bearer 토큰 설정
oauth2_schema = OAuth2PasswordBearer(tokenUrl="/login")

@app.get("/profile/")
async def get_current_user(
        token: str = Depends(oauth2_schema),
        db: AsyncSession = Depends(get_db)):

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        exp = payload.get("exp")

        if username is None:
            raise HTTPException(status_code=401, detail="유효하지않은 토큰")

        if exp is None or datetime.fromtimestamp(exp) < datetime.now():
            raise HTTPException(status_code=401, detail="유효하지않은 토큰")


    except JWTError:
        raise HTTPException(status_code=401, detail="유효하지않은 토큰")

    result = await db.execute( select(User).where(User.username == username))
    user = result.scalar_one_or_none()

    if user is None:
        raise HTTPException(status_code=401, detail="유효하지않은 토큰")
    
    return {
        "id" : user.id,
        "username" : user.username
    }


############################
# pytandics
############################

#request model
class UserRegister(BaseModel):
    username: str
    password: str

    
class UserLogin(BaseModel):
    username: str
    password: str


#response model
class Token(BaseModel):
    access_token: str
    token_type: str



############################
# api
############################

@app.post("/register/")
async def register(
    user: UserRegister,
    db: AsyncSession = Depends(get_db)
):
    
    result = await db.execute(
        select(User).where(User.username == user.username)
    )
    exist_usr = result.scalar_one_or_none()
    if exist_usr:
        raise HTTPException(status_code=400, detail="이미 가입한 사람")


    # 새로운 유저를 db 추가
    new_user = User(
        username = user.username,
        password = hash_password(user.password)
    )

    db.add(new_user)
    await db.commit()
    return {"msg":"Successfully added new user."}




@app.post("/login/", response_model=Token)
async def login(user: UserLogin,
        db: AsyncSession = Depends(get_db)):
    
    result = await db.execute(
        select(User).where(User.username == user.username)
    )
    db_usr = result.scalar_one_or_none()

    # password 매치
    if not db_usr or not verify_password(user.password, db_usr.password):
        raise HTTPException(status_code=401, detail="아이디나 비밀번호가 잘못됨")
    
    access_token = create_access_token({"sub": db_usr.username})


    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/profile/")
async def profile(current_user: dict = Depends(get_current_user)):
    return {
        "username": current_user["username"]
    }




