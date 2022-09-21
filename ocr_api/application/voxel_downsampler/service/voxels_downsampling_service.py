from fastapi import File
import open3d as o3d
from ocr_api.domain.contracts.services.abstract_voxels_downsampling_service import AbstractVoxelDownSampling
from ocr_api.shared.helper.read_files import read_ply_file
from ocr_api.shared.helper.save_files import save_file
from ocr_api.core.point_cloud_visualizer import visualize_point_cloud
from ocr_api.domain.exceptions.pointcloud_exception import VoxelDownSampleException
from ocr_api.domain.models.file_structure import FileStructure
from ocr_api.domain.exceptions.files_exception import FilesException
from ocr_api.persistence.repositories.api_response import ApiResponse
import numpy as np


class VoxelsDownSamplingService(AbstractVoxelDownSampling):
    def voxel_down_sampling(self, path: str, scale: float = 0.5):
        ply = read_ply_file(path)

        try:
            down_ply = ply.voxel_down_sample(voxel_size=scale)
            o3d.io.write_point_cloud(FileStructure.DOWN_SAMPLED_PATH.value + "\\{}-{}".format(path.rpartition('\\')[2],
                                                                                        "downSampled.ply"), down_ply)
            out1 = str(np.shape(ply.points))
            out2 = str(np.shape(down_ply.points))
            return "size input: {} --> size output: {}".format(out1, out2)

        except Exception as e:
            raise VoxelDownSampleException(additional_message="error while DownSampling the file, {}".format(e.__str__()))

