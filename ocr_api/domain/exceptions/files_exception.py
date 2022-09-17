from ocr_api.domain.exceptions.application_error import ApplicationError


class FilesException(ApplicationError):
    def __init__(self, additional_message:str):
        """"
        raised when an error occur during saving/reading files"""
        super().__init__(default_message="Reading/Writing file operation is not valid", additional_message=additional_message)