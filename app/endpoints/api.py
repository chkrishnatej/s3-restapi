from fastapi import APIRouter

from app.endpoints import buckets_info, upload

api_router = APIRouter()

api_router.include_router(buckets_info.router, prefix="/buckets-info", tags=["Buckets Info"])
api_router.include_router(upload.router, prefix="/upload", tags=["Upload data to S3"])
