from fastapi import FastAPI
import asyncio

app = FastAPI()

@app.get("/async-items/")
async def get_async_items():
    await asyncio.sleep(2)
    return {"msg": "This is an async response"}

