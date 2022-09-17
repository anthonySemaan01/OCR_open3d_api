from fileinput import filename

from fastapi import File
import open3d as o3d
from ocr_api.domain.exceptions.pointcloud_exception import PointCloudException


def read_ply_file(path: str) -> o3d.cpu.pybind.geometry.PointCloud:
    try:
        return o3d.io.read_point_cloud(filename=path, format="ply")
    except Exception:
        raise PointCloudException(additional_message="could not read the submitted file")