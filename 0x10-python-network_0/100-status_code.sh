#!/bin/bash
#Send request to the URL and save response to a temporary file
curl -s -o /dev/null -w '%{http_code}' "$1"
