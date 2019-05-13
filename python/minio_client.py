# -*- coding: utf-8 -*-
"""Access data in Minio."""

from minio import Minio
from minio.error import ResponseError
import os

minio_host = "minio.sensemakersams.org"
minio_access_key = "sensemakers"
minio_secret_key = os.environ["PASSWORD"]

minioClient = Minio(minio_host,
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=True)

# List buckets.
buckets = minioClient.list_buckets()
for bucket in buckets:
    print(bucket.name, bucket.creation_date)

# List all object paths in bucket that begin with test.
objects = minioClient.list_objects('backup', prefix='test_project', recursive=True)
for obj in objects:
    print(obj.bucket_name, obj.object_name.encode('utf-8'), obj.last_modified,
          obj.etag, obj.size, obj.content_type)

# Get a full object.
try:
    res = minioClient.get_object('backup', 'test_project/test_device-2019-05-12.json')
    msg_bytes = res.read()
    print(msg_bytes)
except ResponseError as err:
    print(err)
