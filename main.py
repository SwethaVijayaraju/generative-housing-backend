from fastapi import FastAPI
from models.schemas import HousingRequest
import logging

app = FastAPI()

@app.get("/")
def root():
    return "Welcome to generative housing project for small houses! :)"

logging.basicConfig(level=logging.INFO)
@app.post("/generate-layout")
def generate_layout(data: HousingRequest):
    logging.info(f"Received request: {data}")
    return {"msg": "Input received", "rooms": data.rooms}
