from fastapi import APIRouter, HTTPException
from models.schemas import HousingRequest
from services.layout_generator import generate_layout
import logging

router = APIRouter()
logging.basicConfig(level=logging.INFO)


@router.post("/generate-layout")
def generate_layout_endpoint(data: HousingRequest):
    logging.info(f"Received request: {data}")
    placed_rooms = generate_layout(data)
    if not placed_rooms:
        raise HTTPException(status_code=400, detail="No rooms could be placed in the plot")

    return [room.dict() for room in placed_rooms]
