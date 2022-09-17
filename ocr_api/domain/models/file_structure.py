import os
from enum import Enum


class FileStructure(Enum):
    POINT_CLOUD_PATH = "\\".join([os.path.abspath(os.curdir), "datasets", "point-clouds"])
    DOWN_SAMPLED_PATH = "\\".join([os.path.abspath(os.curdir), "datasets", "down-sampled"])
