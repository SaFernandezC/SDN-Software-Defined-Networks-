#!/bin/bash

cp mininet/Controller/* pox/pox/misc/

cd pox
./pox.py log.level --DEBUG openflow.of_01 forwarding.l2_learning misc.firewall