# -*- coding: utf-8 -*-
"""Upload raw messages from a file into InfluxDB."""

from influxdb import InfluxDBClient
import os
import json
import numbers
import click

influxdb_host = "influxdb.sensemakersams.org"
influxdb_port = 443
influxdb_user = "admin"
influxdb_password = os.environ["PASSWORD"]


def raw2point(msg):
    """Convert raw JSON message into an InfluxDB point."""

    msg_json = json.loads(msg)

    # Convert all numeric values to float.
    # This is to avoid type conficts in InfluxDB where the first point written
    # to a series determines the type of the fields.
    for key, value in msg_json["payload_fields"].items():
        if isinstance(value, numbers.Real):
            msg_json["payload_fields"][key] = float(value)

    point = \
        {
            "measurement": msg_json["dev_id"],
            "time": msg_json["time"],
            "tags": {
                "dev_id": msg_json["dev_id"]
            },
            "fields": msg_json["payload_fields"]
        }
    if "tag_fields" in msg_json.keys(): 
        point["tags"].update(msg_json["tag_fields"])

    return point


@click.command()
@click.option('--rawfile', help='Data file with raw messages.')
def upload_file(rawfile):
    """Upload raw messages from a file into InfluxDB."""

    f = open(rawfile, 'r')
    messages = f.readlines()
    points = [raw2point(msg) for msg in messages]
    f.close()

    influxdb_dbname = json.loads(messages[0])["app_id"]

    client = InfluxDBClient(influxdb_host, influxdb_port,
            influxdb_user, influxdb_password, influxdb_dbname,
            ssl=True, verify_ssl=True)

    res = client.write_points(points, time_precision='ms')
    print(f"Wrote {len(messages)} points from {rawfile} into the {influxdb_dbname} database.")


if __name__ == '__main__':
    upload_file()
