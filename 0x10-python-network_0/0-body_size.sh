#!/bin/bash
# Script that takes in a URL, sends a GET request to the URL, and displays size of the body of the response
curl -sI "$1" | grep "Content-length:" | cut -d' ' -f2
