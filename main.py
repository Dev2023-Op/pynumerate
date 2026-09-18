import requests

subdoms = []
target = ""

def subdomains():
	global subdoms
	global target
	with open("subdomains.txt", "r") as file:
		wordlist = file.read().splitlines()
	for item in wordlist:
		r = request.get("https://" + item + "." + target)
		if r.status_code == 301 or r.status_code == 200:
			print("[*] Subdomain Found: https://" + item + "." + target)
