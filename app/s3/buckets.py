from enum import Enum

from botocore.client import BaseClient
from fastapi import Depends

from app.deps import s3_auth


def get_list_of_buckets(s3: BaseClient = Depends(s3_auth)):
    response = s3.list_buckets()
    buckets = {}

    for buckets in response['Buckets']:
        buckets[response['Name']] = response['Name']

    BucketName = Enum('BucketName', buckets)

    return BucketName

