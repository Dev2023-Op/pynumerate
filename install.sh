#!/bin/bash

cd /usr/lib
sudo git clone https://github.com/Dev2023-Op/pynumerate.git && cd pynumerate
sudo python3 -m venv .venv
source .venv/bin/activate
sudo chown -R $USER .venv
pip install requests
pip install python-whois
pip install bs4
sudo mv pynumerate /usr/bin/
sudo chmod 777 /usr/bin/pynumerate
sudo chmod -R a+rX /usr/lib/pynumerate/
