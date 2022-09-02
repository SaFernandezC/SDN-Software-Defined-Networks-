#!/bin/bash

if [ $# -eq 1 ]
then
    echo "Adding $1 more switch to the network"
    echo "..."
    echo "..."
    echo pingall | sudo -E python3 mininet/main.py -n $1
else
    echo pingall | sudo -E python3 mininet/main.py
fi