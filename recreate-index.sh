#!/bin/bash

URL="$ES_PROTO://$ES_HOST:$ES_PORT/$ES_INDEX"

curl -XDELETE "$URL"
echo ''
curl -XPUT -H 'Content-type: application/json' -d '@schema/mapping.json' "$URL"
echo ''
