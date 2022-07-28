#!/bin/bash
# are you well commented
curl -sLIX OPTIONS "$1" | grep "allow" | cut -d ":" -f2
