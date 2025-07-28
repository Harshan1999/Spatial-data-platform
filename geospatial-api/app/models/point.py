from sqlalchemy import Column, Integer, String
from geoalchemy2 import Geometry
from app.database import Base


class Point(Base):
    __tablename__ = "points"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    location = Column(Geometry(geometry_type="POINT", srid=4326))