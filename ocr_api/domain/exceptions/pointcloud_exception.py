from ocr_api.domain.exceptions.application_error import ApplicationError


class PointCloudException(ApplicationError):
    """"
    raised when the point-cloud file is not valid
    """

    def __int__(self, additional_message: str):
        super().__init__("point-cloud file is not valid", additional_message)


class VoxelDownSampleException(ApplicationError):
    """"
    raised when the DownSampling incurred an error
    """

    def __int__(self, additional_message: str):
        super().__init__("DownSampling is not valid", additional_message)

