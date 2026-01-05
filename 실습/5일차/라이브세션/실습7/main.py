from fastapi import FastAPI
from models import Item, Order

app = FastAPI()

@app.post("/orders/")
def create_order(order: Order):
    return {"order": Order}


