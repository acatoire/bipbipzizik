#!/bin/bash
playlist=$1

curl --max-time 2 --silent --output /dev/null -X POST -H "x-ha-access: HOMEASSISTANTPASSWORD" -H "Content-Type: application/json" -d '{"entity_id": "input_text.playlist", "value": "'"$playlist"'"}' http://10.0.0.26:8123/api/services/input_text/set_value
