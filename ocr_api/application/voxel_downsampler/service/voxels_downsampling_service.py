from fastapi import File
import open3d as o3d
from ocr_api.domain.contracts.services.abstract_voxels_downsampling_service import AbstractVoxelDownSampling
from ocr_api.shared.helper.read_files import read_ply_file
from ocr_api.core.point_cloud_visualizer import visualize_point_cloud
from ocr_api.domain.exceptions.pointcloud_exception import VoxelDownSampleException


class VoxelsDownSamplingService(AbstractVoxelDownSampling):
    def voxel_down_sample(self, file: File, scale: float = 0.5):
        try:
            ply = read_ply_file(file)
            down_ply = ply.voxel_down_sample(voxel_size=scale)
            return down_ply
        except Exception:
            raise VoxelDownSampleException(additional_message="error while DownSampling the file")