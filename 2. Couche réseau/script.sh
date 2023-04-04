#!/bin/bash

for file in *.pcap; do
    echo "Analyzing $file ..."
    python script.py "$file"
done
