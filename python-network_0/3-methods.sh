#!/bin/bash
# are you well commented
curl -sI "$1" | grep "allow: " | cut -d " " -f 2-
