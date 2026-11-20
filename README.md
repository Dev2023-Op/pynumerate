# pynumerate
![banner](banner.jpeg)
Pynumerate is a osint tool for web applications that brings most of your scans into one tool. This skips out on the endless tool switching.<br>
![Static Badge](https://img.shields.io/badge/Supported_OS-Linux-red?style=for-the-badge)

## Feature Poll

The next release is version 1.2, if you would like to vote on a feature to be added please go to https://github.com/Dev2023-Op/pynumerate/discussions/24

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

### Installing the latest supported version
1. Click on releases
2. go to the first option that contains the tag Latest
3. download the installer or updater
4. run it as a shell file with ```sudo bash your-installer-file```

To run pynumerate after installation run:
```sh
pynumerate
```

### Supported versions
- Version 1.1

### Installing and Updateing unreleased versions
⚠️ WARNING ⚠️ Only use the below if you are confident in using unsupported versions
```sh
curl https://raw.githubusercontent.com/Dev2023-Op/pynumerate/refs/heads/main/install.sh | bash
```

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
| domain2ip | Retrive a domains host ip |
| ip2domain | Retrive a host ip's domain |
| enumpage | find common pages and directorys |
| services | service detection |
