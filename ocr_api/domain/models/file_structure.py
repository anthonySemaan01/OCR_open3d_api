import os
from enum import Enum


class FileStructure(Enum):
    # Use assets to satore json files of paths for example and then in a service: Parse the file and populate an object.
    POINT_CLOUD_PATH = "\\".join([os.path.abspath(os.curdir), "datasets", "point-clouds"])
    DOWN_SAMPLED_PATH = "\\".join([os.path.abspath(os.curdir), "datasets", "down-sampled"])
