# -*- coding: utf-8 -*-
"""Query data in InfluxDB."""

from influxdb import InfluxDBClient
import os

influxdb_host = "influxdb.sensemakersams.org"
influxdb_port = 443
influxdb_user = "test_project"
influxdb_password = os.environ["PASSWORD"]
influxdb_dbname = "test_project"

client = InfluxDBClient(influxdb_host, influxdb_port,
        influxdb_user, influxdb_password, influxdb_dbname,
        ssl=True, verify_ssl=True)

rs = client.query('SELECT * FROM test_device', epoch='ms')

# Get raw JSON response.
raw = rs.raw

# Get points.
points = rs.get_points(measurement='test_device', tags={'dev_id': 'test_device'})

for point in points:
    print(f"Time: {point['time']}, Temperature: {point['temperature']}")
