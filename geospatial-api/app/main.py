from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import Base, engine, get_db
from app.crud import point as point_crud
from app.crud import polygon as polygon_crud
from app.schemas import point as point_schema
from app.schemas import polygon as polygon_schema

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.post("/points/", response_model=point_schema.PointOut)
def create_point(point: point_schema.PointCreate, db: Session = Depends(get_db)):
    return point_crud.create_point(db, point)


@app.get("/points/", response_model=list[point_schema.PointOut])
def get_points(db: Session = Depends(get_db)):
    return point_crud.get_points(db)


@app.post("/polygons/", response_model=polygon_schema.PolygonOut)
def create_polygon(poly: polygon_schema.PolygonCreate, db: Session = Depends(get_db)):
    return polygon_crud.create_polygon(db, poly)


@app.get("/polygons/", response_model=list[polygon_schema.PolygonOut])
def get_polygons(db: Session = Depends(get_db)):
    return polygon_crud.get_polygons(db)
