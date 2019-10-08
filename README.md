# SURFsara IoT Platform for Sensemakers

Sensemakers make use of the IoT data streaming and analytics platform hosted at SURFsara.

The SURFsara IoT Platform for Sensemakers is a platform for storing, monitoring, visualising and analyzing sensor data. It is a collaboration platform designed to host multiple projects carried by the Sensemakers community. In addition, there is a project dedicated to experimentation, available for everyone to use. All data within the platform is shared.

The platform is built from the following open-source components, deployed as a fault-tolerant service on a Kubernetes cluster:
- **Mosquitto** MQTT broker forms a backbone of the platform.
- Data is stored in files in a shared volume, in an **InfluxDB** time-series database and in a **Minio** object store.
- **Grafana** is available for visualisations and alerting.
- **JupyterHub** provides interface for analytics and investigations with Jupyter notebooks.
- **OpenFaaS** serverless functions give access to the platform through an HTTP entry point, take care of the metadata extraction and enable custom event-driven actions.

This repository is intended for:
- documentation and user guide
- example code showing how to access data
- example Jupyter notebooks
- backups of the Grafana dashboards

**For more general information about the platform, see the [slides from the Sensemakers meetup on 19/06/2019](https://surfdrive.surf.nl/files/index.php/s/h4zsznyea3m8VQI).**

![Platform overview](documentation/sketch-overview.png)
