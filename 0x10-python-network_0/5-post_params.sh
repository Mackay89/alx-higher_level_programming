#!/bin/bash
#Script that takes in a URL, sends a POST requesr to the passed URL, and displays the body of the response
curl -s "$1" -X POST -d "email=testgmail.com&subject=I will always be here for PLD"
