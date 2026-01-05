from fastapi import FastAPI
from model import ContactInfo
app = FastAPI()

@app.post('/contact/')
def create_contact(contact: ContactInfo):
    return {
        "msg": "Contact info accepted",
        "data": contact
    }