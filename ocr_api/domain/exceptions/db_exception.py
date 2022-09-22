from ocr_api.domain.exceptions.application_error import ApplicationError


class DBException(ApplicationError):
    """"
    raised when an error occur while trying to access the DB"""

    def __init__(self, additional_message: str):
        super().__init__(default_message="invalid access to db", additional_message=additional_message)
