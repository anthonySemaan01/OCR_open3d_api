from abc import ABC, abstractmethod


class AbstractVoxelDownSampling(ABC):

    @abstractmethod
    def voxel_down_sampling(self, path: str, scale: float = 0.5):
        pass


