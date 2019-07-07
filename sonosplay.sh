#!/bin/bash

# Get arguments
addr=$1   # Mendatory - exemple : http://192.168.0.140:5005
cmd=$2    # Mendatory - exemple : volume/50


echo "Execute the command '$cmd' on the server at '$addr'"


# Execute the sonos api request using curl

# Clear the queu and load the new album/playlist
# Todo, check if needed for all (maybe not for tracks
# curl -X GET $addr/clearqueue
curl -X GET $addr/$cmd



