from sqlalchemy.orm import Session
from fastapi import UploadFile
from ocr_api.persistence.sqlite_db import point_cloud_model
from ocr_api.persistence.repositories.api_response import ApiResponse


def get_point_clouds(db: Session, skip: int = 0, limit: int = 100):
    return db.query(point_cloud_model.PointCloud).offset(skip).limit(limit).all()


def create_point_cloud(db: Session, point_count: int, path: str):
    point_cloud = point_cloud_model.PointCloud(points_count=point_count, path=path)
    try:
        db.add(point_cloud)
    except Exception as e:
        return ApiResponse(success=False, error=e.__str__())
    db.commit()
    db.refresh(point_cloud)
    return point_cloud
