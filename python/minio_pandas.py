# -*- coding: utf-8 -*-
"""Read data from Minio into Pandas DataFrame.""" 

from minio import Minio
import pandas as pd
import io
import os

minio_host = "minio.sensemakersams.org"
minio_access_key = "sensemakers"
minio_secret_key = os.environ["PASSWORD"]

minioClient = Minio(minio_host,
        access_key=minio_access_key,
        secret_key=minio_secret_key,
        secure=True)

res = minioClient.get_object('backup', 'test_project/test_device-2019-05-12.json')

df = pd.read_json(io.BytesIO(res.data), lines=True)
# Convert time.
df['time'] = pd.to_datetime(df['time'], unit='ms')
# Use time as index.
df.set_index('time', inplace=True)
print(df.head())

# The measured values appear in a single column as embedded JSON.
# Get the measured values as individual columns.
payload_fields = df['payload_fields'].apply(pd.Series)
# Add the new columns to the dataframe and remove the original column with embedded JSON.
df = df.join(payload_fields).drop('payload_fields', axis=1)
print(df.head())
