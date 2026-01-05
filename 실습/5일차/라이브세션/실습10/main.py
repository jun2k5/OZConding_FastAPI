from fastapi import FastAPI
from model import Product
app = FastAPI()

@app.post('/products/')
def create_product(product:Product):
    return product