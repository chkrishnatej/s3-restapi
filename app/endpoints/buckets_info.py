from fastapi import APIRouter, Depends
from app.deps import s3_auth
from botocore.client import BaseClient


router = APIRouter()


@router.get("/")
def get_buckets(s3: BaseClient = Depends(s3_auth)):
    response = s3.list_buckets()

    return response['Buckets']

