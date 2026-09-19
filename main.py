import requests
from fake_useragent import UserAgent
ua = UserAgent()

subdoms = []
target = "torn.com"

def subdomains():
	global subdoms
	global target
	with open("subdomains.txt", "r") as file:
		wordlist = file.read().splitlines()
	headers = {
		"User-Agent": ua.random
	}
	for item in wordlist:
		try:
			r = requests.request(method="GET", url="https://" + item + "." + target, headers=headers)
		except requests.exceptions.RequestException:
			pass
		try:
			
			if r != "":
				if "404" not in r:
					print(f"[*] Subdomain Found: https://{item}.{target}")
		except UnboundLocalError as e:
			pass
		r = ""

subdomains()
