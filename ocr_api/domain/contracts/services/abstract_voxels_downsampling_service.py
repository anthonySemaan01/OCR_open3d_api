from abc import ABC, abstractmethod


class AbstractVoxelDownSampling(ABC):

    @abstractmethod
    def voxel_down_sample(self, path: str, scale: float = 0.5):
        pass


