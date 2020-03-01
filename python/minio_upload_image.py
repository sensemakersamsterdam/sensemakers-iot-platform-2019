# -*- coding: utf-8 -*-
"""Access data in Minio."""

from minio import Minio
from minio.error import ResponseError
import os

minio_host = "minio.sensemakersams.org"
minio_access_key = "astroplant"
minio_secret_key = os.environ["PASSWORD"]

minioClient = Minio(minio_host,
                    access_key=minio_access_key,
                    secret_key=minio_secret_key,
                    secure=True)

try:
    res = minioClient.fput_object('astroplant',
                                  'images/C47C8D65BD76_20180201110010.jpg',
                                  './C47C8D65BD76_20180201110010.jpg',
                                  content_type='image/jpeg')
    print(res)

except ResponseError as err:
    print(err)
