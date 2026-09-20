import requests
import sys
import subprocess

subdoms = []
dirs = []
buckets = []
target = sys.argv[1]

def subdomains():
	global subdoms
	global target
	with open("subdomains.txt", "r") as file:
		wordlist = file.read().splitlines()
	subdoms.append(target)
	headers = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36"
	}
	for item in wordlist:
		try:
			r = requests.request(method="GET", url="https://" + item + "." + target, headers=headers, timeout=0.5)
		except requests.exceptions.RequestException:
			pass
		try:
			
			if r != "":
				if "404" not in r:
					print(f"[*] Subdomain Found: https://{item}.{target}")
					subdoms.append(f"{item}.{target}")
		except UnboundLocalError as e:
			pass
		r = ""
		
def directorys():
	global dirs
	global target
	with open("common.txt", "r") as file:
		wordlist = file.read().splitlines()
	headers = {
		"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36"
	}
	for item in wordlist:
		try:
			r = requests.request(method="GET", url="https://" + target + "/" + item, headers=headers, timeout=0.5)
		except requests.exceptions.RequestException:
			pass
		try:
			
			if r != "":
				if "200" in r:
					print(f"[*] Directory Found: https://{target}/{item}")
					dirs.append(f"{target}/{item}")
		except UnboundLocalError as e:
			pass
		r = ""
		
def s3():
	global subdoms
	for item in subdoms:
		cmd = "aws s3 ls s3://" + item + " --no-sign-request"
		result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
		if "ERROR" not in result.stdout:
			print(f"[*] S3 bucket found: s3://{item}")
	

subdomains()
s3()
exit()
