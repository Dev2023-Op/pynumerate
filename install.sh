#!/bin/bash

cd /usr/lib
sudo git clone https://github.com/Dev2023-Op/pynumerate.git
cd pynumerate
sudo python3 -m venv .venv
sudo source .venv/bin/activate
sudo pip install requests
sudo mv /usr/lib/pynumerate/pynumerate /usr/bin/pynumerate
