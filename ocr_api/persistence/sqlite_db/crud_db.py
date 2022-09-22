from sqlalchemy.orm import Session
from fastapi import UploadFile

import ocr_api.persistence.sqlite_db.point_cloud_model
from ocr_api.persistence.sqlite_db import point_cloud_model
from ocr_api.persistence.repositories.api_response import ApiResponse
from ocr_api.domain.exceptions.db_exception import DBException


def get_point_clouds(db: Session, skip: int = 0, limit: int = 100) -> list:
    try:
        return db.query(point_cloud_model.PointCloud).offset(skip).limit(limit).all()
    except Exception as e:
        raise DBException(additional_message=e.__str__())


def create_point_cloud(db: Session, point_count: int, path: str) -> \
        ocr_api.persistence.sqlite_db.point_cloud_model.PointCloud:
    point_cloud = point_cloud_model.PointCloud(points_count=point_count, path=path)
    try:
        db.add(point_cloud)
        db.commit()
        db.refresh(point_cloud)
        return point_cloud
    except Exception as e:
        raise DBException(additional_message=e.__str__())
