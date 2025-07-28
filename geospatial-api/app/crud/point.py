from sqlalchemy.orm import Session
from app.models.point import Point
from app.schemas.point import PointCreate
from geoalchemy2.shape import from_shape
from shapely.geometry import Point as ShapelyPoint


def create_point(db: Session, point: PointCreate):
    db_point = Point(
        name=point.name,
        location=from_shape(ShapelyPoint(point.coordinates), srid=4326)
    )
    db.add(db_point)
    db.commit()
    db.refresh(db_point)
    return db_point


def get_points(db: Session):
    return db.query(Point).all()


def get_point(db: Session, point_id: int):
    return db.query(Point).filter(Point.id == point_id).first()


def delete_point(db: Session, point_id: int):
    obj = db.query(Point).get(point_id)
    db.delete(obj)
    db.commit()
