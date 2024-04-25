#!/bin/bash
#Script that takes in a URL, sends a request to that URL, and displays size of the body of the response.

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi


response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
if [ "$response" = "200" ]; then 
	curl -s "$1"
fi

