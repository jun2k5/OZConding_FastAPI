from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
def user_info(user_id: int):
    return {"user_id":user_id, "status": "activate"}
