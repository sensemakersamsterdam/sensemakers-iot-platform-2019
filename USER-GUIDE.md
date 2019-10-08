# User guide

This page show how to use individual components of the SURFsara IoT Platform for Sensemakers. The following topics are covered:
- [using MQTT](#mqtt)
- [using InfluxDB](#influxdb)
- [using Minio](#minio)
- [using Grafana](#grafana)
- [using Jupyter](#jupyter)


## MQTT

| | **admin** user | **project1** user | **project2** user | **public** user** |
| :---- | :---- | :---- | :---- | :---- |
| **public** topic | read/write | read/write | read/write | read/write |
| **pipeline/project1** topic | read/write | read/write | read-only | read-only |
| **pipeline/project2** topic | read/write | read-only | read/write | read-only |
| **project1** topic | read/write | read/write | no access | no access |
| **project2** topic | read/write | no access | read/write | no access | 

```
mosquitto_sub -t public -h mqtt.sensemakersams.org -p 9998 -u public -P $PUBLIC_PASSWORD
mosquitto_pub -t public -m 42 -h mqtt.sensemakersams.org -p 9998 -u public -P $PUBLIC_PASSWORD

mosquitto_sub -t pipeline/# -h mqtt.sensemakersams.org -p 9998 -u public -P $PUBLIC_PASSWORD
```


## InfluxDB

Every projects is given project-specific user and database in InfluxDB. Messages sent to the [automated data pipeline](DATA.md#automated-data-pipeline) are stored in the database related to the project. All values in a message are stored in the time series belonging to the device.

The following table shows the access rights for different users:

| | **admin** user | **project1** user | **project2** user | **public** user** |
| :---- | :---- | :---- | :---- | :---- |
| **project1** database | read/write | read-only | no access | no access |
| **project2** database | read/write | no access | read-only | no access |

Data can be accessed using the [influx command line client](https://docs.influxdata.com/influxdb/v1.7/tools/shell/).

First, connect to the database in InfluxDB for your project:

```sh
influx -host influxdb.sensemakersams.org \
	-port 443 -ssl \
	-username $PROJECT_NAME \
	-password $PROJECT_PASSWORD \
	-database $PROJECT_NAME
```

Next, show the available measurements and series:

```
> SHOW MEASUREMENTS
> SHOW SERIES
```

Make sure timestamps are shown human-readable:

```
> precision rfc3339
```

Inspect tags:

```
> SHOW TAG KEYS
> SHOW TAG KEYS FROM "357518080332281"
> SHOW TAG VALUES WITH KEY = "name"
> SHOW TAG VALUES FROM "357518080332281" WITH KEY = "name"
```

Show what quantities are measured by individual devices. The first example shows the quantities for all devices, the second example shows only the quantites from the device called `357518080332281`.

```
> SHOW FIELD KEYS
> SHOW FIELD KEYS FROM "357518080332281"
```

Some example queries:

```
> SELECT * FROM "357518080332281"
> SELECT * FROM /.*/ ORDER BY DESC LIMIT 1
> SELECT waterTemperature FROM "357518080332281"
```

The influx client can be used to download data in a CSV or JSON format:

```sh
> influx -host influxdb.sensemakersams.org \
	-port 443 -ssl \
	-username $PROJECT_NAME \
	-password $PROJECT_PASSWORD \
	-database $PROJECT_NAME \
    -precision rfc3339 \
	-execute "SELECT * FROM \"357518080332281\"" -format csv
name,time,FixAge,Lat,Lon,SatInFix,TimeActive,altitude,batteryVoltage,boardTemperature,course,dev_id,imei,lastResetCause,name,speed,timestamp,waterEC,waterTemperature
357518080332281,2019-07-10T00:41:19.831Z,255,0.0000255,0.0000255,0,26231,0,3.96,24,0,357518080332281,357518080332281,32,EC 242,0,1562719373,0,22.85
357518080332281,2019-07-10T00:56:19.83Z,255,0.0000255,0.0000255,0,27131,0,3.96,24,0,357518080332281,357518080332281,32,EC 242,0,1562720273,0,22.85
357518080332281,2019-07-10T01:26:31.395Z,255,0.0000255,0.0000255,0,28930,0,3.96,24,0,357518080332281,357518080332281,32,EC 242,0,1562722072,3,22.85
357518080332281,2019-07-10T01:56:19.455Z,255,0.0000255,0.0000255,0,30730,0,3.96,24,0,357518080332281,357518080332281,32,EC 242,0,1562723872,0,22.94
357518080332281,2019-07-10T02:26:19.146Z,255,0.0000255,0.0000255,0,32530,0,3.96,24,0,357518080332281,357518080332281,32,EC 242,0,1562725672,0,22.94
357518080332281,2019-07-10T02:41:19.817Z,255,0.0000255,0.0000255,0,33431,0,3.96,24,0,357518080332281,357518080332281,32,EC 242,0,1562726573,0,22.94
357518080332281,2019-07-10T02:56:19.121Z,255,0.0000255,0.0000255,0,34331,0,3.96,23,0,357518080332281,357518080332281,32,EC 242,0,1562727473,0,22.85
357518080332281,2019-07-10T03:26:19.089Z,255,0.0000255,0.0000255,0,36131,0,3.96,24,0,357518080332281,357518080332281,32,EC 242,0,1562729273,1,22.94
357518080332281,2019-07-10T03:41:19.249Z,255,0.0000255,0.0000255,0,37031,0,3.96,24,0,357518080332281,357518080332281,32,EC 242,0,1562730173,0,22.85
```

Alternatively, one can interact with the database through [InfluxDB HTTP endponts](https://docs.influxdata.com/influxdb/v1.7/tools/api/). An example query is given below.

```sh
> curl "https://influxdb.sensemakersams.org/query?u=$PROJECT_NAME&p=$PROJECT_PASSWORD" \
    --data-urlencode "db=$PROJECT_NAME" \
    --data-urlencode "q=SHOW MEASUREMENTS"
```


## Minio

| | **admin** user | **public** user |
| :---- | :---- | :---- |
| **data** bucket | read/write | read-only |
| **metadata** bucket | read/write | read-only |


## Grafana

| | **admin** user | **project1** user | **project2** user | **public** user** |
| :---- | :---- | :---- | :---- | :---- |
| **monitoring** folder | view/edit | no access | no access | no access |
| **project1** folder | view/edit | view/edit | view | view |
| **project2** folder | view/edit | view | view/edit | view |


## Jupyter