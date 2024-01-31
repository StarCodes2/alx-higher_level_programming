#!/bin/bash
# Sends a JSON POST request to a given URL, passed a json as its second argument
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
