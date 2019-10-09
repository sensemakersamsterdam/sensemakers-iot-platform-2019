#!/bin/bash
if [ $# -lt 2 ]
then
  exit 1
fi

# Get project name and dashboard json from command line arguments.
export PROJECT_NAME=$1
export DASHBOARD_JSON=$2

# Get project folder identifier.
export FOLDER_ID=$(curl https://grafana.sensemakersams.org/api/folders -u "admin:$PASSWORD" | jq '.[] | select(.title == "'$PROJECT_NAME'") | .id' | tr -d '"')
echo $FOLDER_ID

# Add foder id to the dashboard JSON.
jq --argjson folderId "$FOLDER_ID" '. + {folderId: $folderId}' $DASHBOARD_JSON > dashboard.json

# Add the dashboard for the project.
curl --fail -XPOST \
  -H "Accept: application/json" -H "Content-Type: application/json" \
  -u "admin:$PASSWORD" \
  https://grafana.sensemakersams.org/api/dashboards/db \
  --data @dashboard.json | jq .

curl https://grafana.sensemakers.sda-projects.nl/api/search?folderIds=$FOLDER_ID -u "admin:$PASSWORD" | jq .
