# -*- coding: utf-8 -*-
"""Read data from InfluxDB into Pandas DataFrame."""

from influxdb import DataFrameClient
import os

influxdb_host = "influxdb.sensemakersams.org"
influxdb_port = 443
influxdb_user = "test_project"
influxdb_password = os.environ["PASSWORD"]
influxdb_dbname = "test_project"

client = DataFrameClient(influxdb_host, influxdb_port,
        influxdb_user, influxdb_password, influxdb_dbname,
        ssl=True, verify_ssl=True)

# Query returns a dictionary of dataframes.
rs = client.query('SELECT * FROM test_device')

df = rs['test_device']
print(df.head())
