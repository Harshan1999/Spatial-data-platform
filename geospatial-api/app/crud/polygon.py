from sqlalchemy.orm import Session
from app.models.polygon import Polygon
from app.schemas.polygon import PolygonCreate
from geoalchemy2.shape import from_shape
from shapely.geometry import Polygon as ShapelyPolygon


def create_polygon(db: Session, poly: PolygonCreate):
    db_polygon = Polygon(
        name=poly.name,
        boundary=from_shape(ShapelyPolygon(poly.coordinates), srid=4326)
    )
    db.add(db_polygon)
    db.commit()
    db.refresh(db_polygon)
    return db_polygon


def get_polygons(db: Session):
    return db.query(Polygon).all()


def get_polygon(db: Session, polygon_id: int):
    return db.query(Polygon).filter(Polygon.id == polygon_id).first()


def delete_polygon(db: Session, polygon_id: int):
    obj = db.query(Polygon).get(polygon_id)
    db.delete(obj)
    db.commit()