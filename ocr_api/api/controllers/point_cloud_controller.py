from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from ocr_api.containers import Services
from ocr_api.domain.exceptions.pointcloud_exception import VoxelDownSampleException
from ocr_api.shared.helper.save_files import save_file
from ocr_api.domain.models.file_structure import FileStructure
from ocr_api.domain.exceptions.files_exception import FilesException
from ocr_api.persistence.repositories.api_response import ApiResponse
from ocr_api.persistence.sqlite_db import crud_db, point_cloud_model
from ocr_api.persistence.sqlite_db.database import SessionLocal, engine
import numpy as np
from sqlalchemy.orm import Session
from ocr_api.shared.helper import read_files
from ocr_api.domain.exceptions.db_exception import DBException

router = APIRouter()

voxel_downsampling_service = Services.voxels_downsampling_service()


# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post('/DownSampling')
async def reduce_points(point_cloud_file: UploadFile, ratio: float = 0.5, db: Session = Depends(get_db)):
    try:
        path_to_file = save_file(upload_file=point_cloud_file, destination=str(FileStructure.POINT_CLOUD_PATH.value))
        datas = voxel_downsampling_service.voxel_down_sampling(path=path_to_file, scale=ratio)
        db_point_cloud = crud_db.create_point_cloud(db=db, point_count=datas["input"]["size"],
                                                    path=datas["input"]["path"])
        db_point_cloud = crud_db.create_point_cloud(db=db, point_count=datas["output"]["size"],
                                                    path=datas["output"]["path"])
        return ApiResponse(
            success=True, data=datas
        )

    except VoxelDownSampleException as e:
        return ApiResponse(
            success=False, error=e.__str__()
        )
    except FilesException as e:
        return ApiResponse(
            success=False, error=e.__str__()
        )
    except Exception as e:
        return ApiResponse(
            success=False, error=e.__str__()
        )


@router.post('/PointCloud')
async def create_point_cloud(point_cloud_file: UploadFile = File(...), db: Session = Depends(get_db)):
    try:
        path_to_file = save_file(upload_file=point_cloud_file, destination=str(FileStructure.POINT_CLOUD_PATH.value))
        ply = read_files.read_ply_file(path_to_file)
        point_count = np.shape(ply.points)[0] * np.shape(ply.points)[1]
        db_point_cloud = crud_db.create_point_cloud(db=db, point_count=point_count, path=path_to_file)

    except FilesException as e:
        return ApiResponse(success=False, error=e.__str__())

    except DBException as e:
        return ApiResponse(success=False, error=e.__str__())

    except Exception as e:
        return ApiResponse(success=False, error=e.__str__())

    return db_point_cloud


@router.get("/PointCloud")
async def get_point_clouds(db: Session = Depends(get_db)):
    try:
        point_clouds = crud_db.get_point_clouds(db=db)
        if point_clouds is None:
            return HTTPException(status_code=400, detail="there is no point_clouds")
        return point_clouds
    except DBException as e:
        return ApiResponse(success=False, error=e.__str__())

    except Exception as e:
        return ApiResponse(success=False, error=e.__str__())


