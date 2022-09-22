from fileinput import filename

from fastapi import File
import open3d as o3d
from ocr_api.domain.exceptions.files_exception import FilesException


def read_ply_file(path: str) -> o3d.cpu.pybind.geometry.PointCloud:
    try:
        return o3d.io.read_point_cloud(path, format="ply")
    except Exception as e:
        raise FilesException(additional_message="error while reading file from {}; {}".format(path, e.__str__()))