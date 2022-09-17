from fastapi import APIRouter, HTTPException, UploadFile, File
from ocr_api.containers import Services
from ocr_api.domain.exceptions.pointcloud_exception import VoxelDownSampleException
from ocr_api.shared.helper.save_files import save_file
from ocr_api.domain.models.file_structure import FileStructure
from ocr_api.domain.exceptions.files_exception import FilesException
from ocr_api.persistence.repositories.api_response import ApiResponse
router = APIRouter()

voxel_downsampling_service = Services.voxels_downsampling_service()


@router.post('/DownSampling')
async def reduce_points(point_cloud_file: UploadFile, ratio: float = 0.5):
    try:
        path_to_file = save_file(upload_file=point_cloud_file, destination=str(FileStructure.POINT_CLOUD_PATH.value))
        datas = voxel_downsampling_service.voxel_down_sampling(path=path_to_file, scale=ratio)
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
