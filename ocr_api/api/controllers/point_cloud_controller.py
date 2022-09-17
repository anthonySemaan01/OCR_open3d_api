from fastapi import APIRouter, HTTPException, UploadFile, File
from ocr_api.containers import Services
from ocr_api.domain.exceptions.pointcloud_exception import VoxelDownSampleException
from ocr_api.shared.helper.save_files import save_file
from ocr_api.domain.models.file_structure import FileStructure

router = APIRouter()

voxel_downsampling_service = Services.voxels_downsampling_service()


@router.post('/DownSampling')
async def reduce_points(point_cloud_file: UploadFile, ratio: float = 0.5):
    save_file(upload_file=point_cloud_file, destination=str(FileStructure.POINT_CLOUD_PATH.value))
    return point_cloud_file.filename
    # try:
    #     voxel_downsampling_service.voxel_down_sample(file=point_cloud_file, scale=ratio)
    # except VoxelDownSampleException as e:
    #     raise HTTPException(status_code=404, detail=e.__str__())
    # except Exception as e:
    #     raise HTTPException(status_code=400, detail=e.__str__())
