# Python code examples

The following examples are given:
- Publish data to an MQTT topic.
- Subscribe to an MQTT topic.
- Query data in InfluxDB.
- Read data from InfluxDB into Pandas DataFrame.
- Access data in Minio.
- Read data from Minio into Pandas DataFrame. 

Make a dedicated python virtual environment with the packages needed to run the examples here.

https://virtualenvwrapper.readthedocs.io/en/latest/

```
mkvirtualenv sensemakers
pip install -r requirements.txt
```

Activate the environment every time you start.

```
workon sensemakers
```

The example scripts look read credentials from an environment variable.

```
export PASSWORD=1234
```

Useful links:
- https://github.com/eclipse/paho.mqtt.python/tree/master/examples
- https://influxdb-python.readthedocs.io/en/latest/examples.html
- https://docs.min.io/docs/python-client-api-reference.html
