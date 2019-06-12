# Grafana dashboards

List dashboards in Grafana.

```
curl https://grafana.sensemakersams.org/api/search -u "admin:1234" | jq .
```

Download a dasbhoard from Grafana using its unique identifier.

```
curl https://grafana.sensemakersams.org/api/dashboards/uid/L8fQTXiZz -u "admin:1234" | jq . > dashboard.json
curl https://grafana.sensemakersams.org/api/dashboards/uid/m2HAkciWk -u "admin:1234" | jq . > dashboard.json
```

Remove the `id` field from the JSON file and import the dashboard.

```
curl -XPOST \
  -H "Accept: application/json" -H "Content-Type: application/json" \
  -u "admin:1234" \
  https://grafana.sensemakersams.org/api/dashboards/db \
  --data @dashboard.json | jq .
```
