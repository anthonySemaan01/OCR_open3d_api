import uvicorn
from fastapi import FastAPI, Depends
from starlette.middleware.cors import CORSMiddleware
from api.controllers import health_check_controller, point_cloud_controller
import sys
from ocr_api.persistence.sqlite_db import point_cloud_model
from ocr_api.persistence.sqlite_db.database import engine, SessionLocal

app = FastAPI(version='1.0', title='OCR Open-3d player',
              description="API for reducing the number of cloud points")

point_cloud_model.Base.metadata.create_all(bind=engine) # Check if can be moved to persistence/database.py


app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )

app.include_router(
    router=health_check_controller.router,
    prefix="/health",
    tags=["health"],
)

app.include_router(
    router=point_cloud_controller.router,
    prefix="/Services",
    tags=["Services"],
)

if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=5555)
