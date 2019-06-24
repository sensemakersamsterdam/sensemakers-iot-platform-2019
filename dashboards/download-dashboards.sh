#!/bin/bash

uids=$(curl -s https://grafana.sensemakersams.org/api/search -u "admin:$PASSWORD" | jq '.[].uid' | tr -d '"')

for uid in $uids
do
  curl -s https://grafana.sensemakersams.org/api/dashboards/uid/$uid -u "admin:$PASSWORD" | jq . > dashboard-$uid.json
  jq '.dashboard.id=null' dashboard-$uid.json | sponge dashboard-$uid.json
  jq 'del(.meta)' dashboard-$uid.json | sponge dashboard-$uid.json
  echo dashboard-$uid.json $(jq .'dashboard.title' dashboard-$uid.json)
done
