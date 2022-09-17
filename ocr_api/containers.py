from dependency_injector import containers, providers
from ocr_api.domain.contracts.services.abstract_voxels_downsampling_service import AbstractVoxelDownSampling
from application.voxel_downsampler.service.voxels_downsampling_service import VoxelsDownSamplingService


class Services(containers.DeclarativeContainer):

    # extractor
    voxels_downsampling_service = providers.Factory(
        AbstractVoxelDownSampling.register(VoxelsDownSamplingService))

