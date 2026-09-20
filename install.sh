#!/bin/bash

cd /usr/lib
sudo git clone https://github.com/Dev2023-Op/pynumerate.git && cd pynumerate
sudo python3 -m venv .venv
source .venv/bin/activate
sudo chown -R $USER .venv
pip install requests
sudo mv pynumerate /usr/bin/
sudo chmod +x /usr/bin/pynumerate
