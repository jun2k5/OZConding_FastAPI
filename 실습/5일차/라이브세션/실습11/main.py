from fastapi import FastAPI
from model import User

app = FastAPI()

@app.post('/users/')
def create_user(user:User):
    return {"user": user}
