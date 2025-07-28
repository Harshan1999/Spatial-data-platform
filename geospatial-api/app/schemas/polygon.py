from pydantic import BaseModel
from typing import List, Tuple


class PolygonCreate(BaseModel):
    name: str
    coordinates: List[Tuple[float, float]]  # [(lng, lat), (lng, lat), ...]


class PolygonOut(PolygonCreate):
    id: int

    class Config:
        orm_mode = True