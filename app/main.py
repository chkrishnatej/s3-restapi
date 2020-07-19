from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.endpoints.api import api_router

app = FastAPI(title="S3 Buckets Info",description="Simple S3 Buckets uploader",
              openapi_url=f"/openapi.json")

app.include_router(api_router)
