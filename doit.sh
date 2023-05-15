#!/bin/sh
source .env
python3 set-sw-hostnames.py
read -p "Change vpn and press enter to continue"
python3 set-sw-hostnames2.py
