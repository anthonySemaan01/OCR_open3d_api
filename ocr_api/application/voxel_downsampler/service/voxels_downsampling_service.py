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
    # If it uses another service, then we need to create a constructor __init__ and feed services or what is needed

    def voxel_down_sampling(self, path: str, scale: float = 0.5) # Always add return type -> type:
        ply = read_ply_file(path)

        try:
            down_ply = ply.voxel_down_sample(voxel_size=scale)
            output_path = FileStructure.DOWN_SAMPLED_PATH.value + "\\{}-{}".format(path.rpartition('\\')[2],
                                                                                   "downSampled.ply")
                                                                                   # Use os.path.join
            o3d.io.write_point_cloud(output_path, down_ply)
            out1 = np.shape(ply.points) # Add variable type out1: int = ...
            out2 = np.shape(down_ply.points)

            # Use models instead of json
            #class PCInformation(pydantic):
            #    input: Dict[str,str]
            #    output: Dict[str,str]

            return {
                "input": {
                    "size": out1,
                    "path": path
                },
                "output": {
                    "size": out2,
                    "path": output_path
                }
            }

        except Exception as e:
            raise VoxelDownSampleException(
                additional_message="error while DownSampling the file, {}".format(e.__str__()))
