from pydantic import BaseModel
from typing import List, Dict, Optional


class Room(BaseModel):
    name: str
    min_area: float
    width: Optional[float] = None
    depth: Optional[float] = None
    x: Optional[float] = None  # X-coordinate position
    y: Optional[float] = None  # Y-coordinate position


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
