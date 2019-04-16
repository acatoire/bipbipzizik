#!/bin/bash

# Get arguments
addr=$1   # Mendatory - exemple : http://192.168.0.140:5005
cmd=$2    # Mendatory - exemple : volume/50
#where=$3 # Optional - exemple : salon TODO

# Execut the sonos api request using curl
curl -X GET $addr/$cmd todo add where as optional
#curl -X GET $addr/$where/$cmd TODO add $where as optional
