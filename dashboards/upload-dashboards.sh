#!/bin/bash

dashboards=$(ls dashboard-*.json)

for dashboard in $dashboards
do
  curl -s -XPOST \
    -H "Accept: application/json" -H "Content-Type: application/json" \
    -u "admin:$PASSWORD" \
    https://grafana.sensemakersams.org/api/dashboards/db \
    --data @$dashboard | jq .
done
