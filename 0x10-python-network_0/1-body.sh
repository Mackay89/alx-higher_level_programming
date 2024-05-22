#!/bin/bash
# Script that takes in a URL, sends a GET request to the URL, and displays the body of the response
curl -sSl "$1" -X GET -D ./header -o ./output; if grep -q "200 OK" ./header; then cat ./output; fi