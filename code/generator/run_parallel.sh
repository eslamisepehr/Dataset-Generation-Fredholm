#!/bin/bash

NUM_SESSIONS=32

SCRIPT_TO_RUN="run.sh"

for ((i=0; i<NUM_SESSIONS; i++)); do
    screen -S "session_$i" -dm bash -c "/home/ubuntu/research/run.sh; exec bash"

    echo "Created screen session session_$i and started $SCRIPT_TO_RUN"
done

echo "All screen sessions created."
