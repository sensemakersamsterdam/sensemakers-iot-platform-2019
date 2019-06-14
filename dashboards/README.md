# Grafana dashboards

List dashboards in Grafana.

```
export PASSWORD=1234

curl https://grafana.sensemakersams.org/api/search -u "admin:$PASSWORD" | jq .
```

Download a dasbhoard from Grafana using its unique identifier.

```
curl https://grafana.sensemakersams.org/api/dashboards/uid/L8fQTXiZz -u "admin:$PASSWORD" | jq . > dashboard.json
curl https://grafana.sensemakersams.org/api/dashboards/uid/m2HAkciWk -u "admin:$PASSWORD" | jq . > dashboard.json
```

When importing dashboards, the `id` field should be removed as it is an auto-incrementing numeric value unique per Grafana install.
For dashboard provisioning, the unique identifired `uid` is important when syncing dashboards amonng multiple Grafana installs.

https://grafana.com/docs/http_api/dashboard/#identifier-id-vs-unique-identifier-uid

Remove the `id` field from the JSON file.

```
jq '.dashboard.id=null' dashboard.json | sponge dashboard.json
```

Import the dashboard.

```
curl -XPOST \
  -H "Accept: application/json" -H "Content-Type: application/json" \
  -u "admin:$PASSWORD" \
  https://grafana.sensemakersams.org/api/dashboards/db \
  --data @dashboard.json | jq .
```
