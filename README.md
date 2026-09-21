# pynumerate

Pynumerate is a automated osint tool for web applications.

Pynumerate finds:
- subdomains
- s3 buckets

## Success Criteria
- [ ] must use a shell like interface
- [ ] must have modules
- [ ] must have module detection
- [ ] must have a search interface

## Disclaimer
This tool is intended for legal and ethical use only. The contributors and or owner of this repository will not cover or recive publicity for consequences caused by this tool.

## Installation

### Requirements
- python3
- python3-pip
- git
- curl

```sh
curl https://raw.githubusercontent.com/Dev2023-Op/pynumerate/refs/heads/main/install.sh | sudo bash
```

## Usage

```sh
pynumerate <target url>
# make sure you remove the http/https part aswell as the www part unless your targeting that subdomain
```
