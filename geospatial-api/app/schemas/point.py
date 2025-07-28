from pydantic import BaseModel
from typing import Tuple


class PointCreate(BaseModel):
    name: str
    coordinates: Tuple[float, float]  # (longitude, latitude)


class PointOut(PointCreate):
    id: int

    class Config:
        orm_mode = True
