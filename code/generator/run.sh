#!/bin/bash

while true; do
    timeout 7s python3 second_kind_Fredholm.py

    if [ $? -eq 124 ]; then
        echo "Script timed out"
    else
        echo "Script completed"
    fi
done