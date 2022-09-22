import json
import os

from fastapi import UploadFile
import shutil
from ocr_api.domain.exceptions.files_exception import FilesException


def save_file(upload_file: UploadFile, destination: str) -> str:
    try:
        with open(destination + "\\" + upload_file.filename, "wb+") as file_object:
            shutil.copyfileobj(upload_file.file, file_object)

    except Exception as e:
        raise FilesException(additional_message="error while saving file to {}; {}".format(destination, e.__str__()))
    return destination + "\\" + upload_file.filename
