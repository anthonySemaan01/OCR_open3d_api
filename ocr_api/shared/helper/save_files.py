import json
import os

from fastapi import UploadFile
import shutil
from ocr_api.domain.exceptions.application_error import ApplicationError


def save_file(upload_file: UploadFile, destination: str) -> json:
    print(os.listdir(destination))
    try:
        with open(destination + "\\" + upload_file.filename, "wb+") as file_object:
            shutil.copyfileobj(upload_file.file, file_object)

    except Exception:
        raise ApplicationError(default_message="Error while saving the file", additional_message="check the save file"
                                                                                                 "helper function")

    return {"info": f"file '{upload_file.filename}' saved at '{destination}'"}
