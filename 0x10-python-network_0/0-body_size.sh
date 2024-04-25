#!/usr/bin/python3
#Script that takes in a URL, sends a request to that URL, and displays size of the body of the response.

if [ -z "$1" ]; then
	echo "Usage: $0 <URL>"
	exit 1
if

curl -s "$1" | wc -c 
