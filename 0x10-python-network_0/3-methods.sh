#!/bin/bash
# Take a URL and displays all HTTP methods the server will accept
curl -sI | grep "ALLOW" | cut -d " " -f 2
