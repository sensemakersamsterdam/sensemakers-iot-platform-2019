#!/bin/bash
if [ $# -lt 1 ]
then
  exit 1
fi

# Get dashboard unique identifier from command line arguments.
uid=$1

curl https://grafana.sensemakers.sda-projects.nl/api/dashboards/uid/$uid -u "admin:$PASSWORD" | jq . > dashboard-$uid.json
jq '.dashboard.id=null' dashboard-$uid.json | sponge dashboard-$uid.json
jq 'del(.meta)' dashboard-$uid.json | sponge dashboard-$uid.json
