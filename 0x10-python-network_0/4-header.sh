#!/bin/bash
#Script that takes in a URL as an argument,sends a GET request to the URL, and displaysthe body of the response.
curl -s "$1" -X GET -H "X-School-User-Id: 98"
