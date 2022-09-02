#!/bin/bash
(echo "h1 iperf -s -p 80 &" && echo "h3 iperf -c 10.0.0.1 -p 80 -n 1024") | sudo -E python3 mininet/main.py