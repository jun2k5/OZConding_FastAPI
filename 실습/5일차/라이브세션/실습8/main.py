from fastapi import FastAPI
from model import Reservation

app = FastAPI()

@app.post("/reservations/")
def create_reservation(reservation: Reservation):
    return {"reservation": reservation}