#!/bin/bash
# Sends a request to 0.0.0.0:5000/catch_me
curl -sL -H "Origin: HolbertonSchool" -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
