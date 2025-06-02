from pydantic import BaseModel
from typing import List, Dict

class Room(BaseModel):
    type: str
    min_area: float

class Setbacks(BaseModel):
    front: float
    back: float
    sides: float

class Plot(BaseModel):
    width: float
    depth: float

class HousingRequest(BaseModel):
    plot: Plot
    setbacks: Setbacks
    rooms: List[Room]
    orientation: str
