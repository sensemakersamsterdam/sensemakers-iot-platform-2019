# Grafana dashboards

List dashboards in Grafana.

```
export PASSWORD=1234

curl https://grafana.sensemakersams.org/api/search -u "admin:$PASSWORD" | jq .
```

Download a dasbhoard from Grafana using its unique identifier.

```
# Rain gauge
curl https://grafana.sensemakersams.org/api/dashboards/uid/L8fQTXiZz -u "admin:$PASSWORD" | jq . > dashboard.json
# Mijn Omgeving
curl https://grafana.sensemakersams.org/api/dashboards/uid/m2HAkciWk -u "admin:$PASSWORD" | jq . > dashboard.json
# MQTT dashboard
curl https://grafana.sensemakersams.org/api/dashboards/uid/jBA4zlVWk -u "admin:$PASSWORD" | jq . > dashboard.json
```

When importing dashboards, the `id` field should be removed as it is an auto-incrementing numeric value unique per Grafana install.
For dashboard provisioning, the unique identifired `uid` is important when syncing dashboards amonng multiple Grafana installs.

https://grafana.com/docs/http_api/dashboard/#identifier-id-vs-unique-identifier-uid

Remove the `id` field from the JSON file. Metadata can be also removed.

```
jq '.dashboard.id=null' dashboard.json | sponge dashboard.json
jq 'del(.meta)' dashboard.json | sponge dashboard.json
```

Get project folder identifier and add it to the dashboard JSON.

```
export FOLDER_ID=$(curl https://grafana.sensemakersams.org/api/folders -u "admin:$PASSWORD" | jq '.[] | select(.title == "'$PROJECT_NAME'") | .id' | tr -d '"')
echo $FOLDER_ID

jq --argjson folderId "$FOLDER_ID" '. + {folderId: $folderId}' $DASHBOARD_JSON > dashboard.json
```

Import the dashboard.

```
curl -XPOST \
  -H "Accept: application/json" -H "Content-Type: application/json" \
  -u "admin:$PASSWORD" \
  https://grafana.sensemakersams.org/api/dashboards/db \
  --data @dashboard.json | jq .
```

The above can be achieved by the scripts from this folder.

```
# Rain gauge
./download-dashboard.sh L8fQTXiZz
# Mijn Omgeving
./download-dashboard.sh m2HAkciWk
# WON workshop
./download-dashboard.sh BQjQi9KZk

./upload-dashboard.sh test_project dashboard-L8fQTXiZz.json
./upload-dashboard.sh mijnomgeving dashboard-m2HAkciWk.json
./upload-dashboard.sh WON dashboard-BQjQi9KZk.json
```
