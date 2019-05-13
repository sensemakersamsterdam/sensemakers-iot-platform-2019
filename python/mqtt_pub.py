# -*- coding: utf-8 -*-
"""Publish data to an MQTT topic."""

import paho.mqtt.publish as publish
import os
import json
import time

mqtt_host = "lb.cluster-meetup-demo.aws.surfsaralabs.nl"
mqtt_port = 9998
mqtt_user = "public"
mqtt_password = os.environ["PASSWORD"]

msg_json = {
    "app_id": "test_project", "dev_id": "test_device",
    "payload_fields": {"temperature": 42, "co2": 42},
    "time": int(time.time() * 1e3)
}
msg_str = json.dumps(msg_json)

auth = {"username": mqtt_user, "password": mqtt_password}
publish.single("public", payload=msg_str, hostname=mqtt_host, port=mqtt_port, auth=auth)
