# pynumerate
![banner](banner.jpeg)
Pynumerate is a osint tool for web applications that brings most of your scans into one tool. This skips out on the endless tool switching.<br>
![Static Badge](https://img.shields.io/badge/Supported_OS-Linux-red?style=for-the-badge)
![Endpoint Badge](https://img.shields.io/endpoint?url=https%3A%2F%2Fghloc.dev%2Fapi%2FDev2023-Op%2Fpynumerate%2Fbadge&style=for-the-badge&color=red)

## Contents
- [Disclaimer](#disclaimer)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)

## Disclaimer
This tool is intended for legal and ethical use only. The contributors and or owner of this repository will not cover or recive publicity for consequences caused by this tool.

## Installation

### Requirements
- python3
- python3-pip
- aws cli
- git
- curl

```sh
curl https://raw.githubusercontent.com/Dev2023-Op/pynumerate/refs/heads/main/install.sh | bash
```

## Updateing
```sh
curl https://raw.githubusercontent.com/Dev2023-Op/pynumerate/refs/heads/main/update.sh | bash
```

## Usage
To start:
```sh
pynumerate
```
For more information:
```sh
(pynumerate)> help
```

## Modules

pynumerate runs on modules witch are small programs that assist your program.

### Preinstalled modules
| Module | Function |
|---|---|
| Basic | Perform a subdomain scan then scan those subdomains for public s3 |
| subdomains | Enumerate common subdomains |
| s3 | check a domain or subdomain for s3 |
| whois | Retrive whois data for a website |
| domain2ip| Retrive a domains host ip |
| ip2domain| Retrive a host ip's domain |
