#!/usr/bin/env bash
# Sends a GET request to a URL and displays the response status code
curl -s -o /dev/null -w "%{http_code}" "$1"
