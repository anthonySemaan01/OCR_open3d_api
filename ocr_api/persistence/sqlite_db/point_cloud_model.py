from sqlalchemy import Column, Integer, String
from ocr_api.persistence.sqlite_db.database import Base


class PointCloud(Base):
    __tablename__ = "point_clouds"

    id = Column(Integer, primary_key=True, index=True)
    points_count = Column(Integer, primary_key=False, index=True)
    path = Column(String, unique=False, index=True)
