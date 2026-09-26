import sys
import requests

subdoms = []

try:
	target = sys.argv[1]
except IndexError:
	target = input("Whats the URL your testing? ")

try:
	with open("modules/basic/subdomains.txt", "r") as file:
		wordlist = file.read().splitlines()
except FileNotFoundError:
	try:
		with open("subdomains.txt", "r") as file:
			wordlist = file.read().splitlines()
	except FileNotFoundError:
		print("[ERROR] subdomains wordlist not found")
subdoms.append(target)
headers = {
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36"
}
for item in wordlist:
	try:
		r = requests.request(method="GET", url="https://" + item + "." + target, headers=headers, timeout=0.5)
	except requests.exceptions.RequestException:
		try:
			r = requests.request(method="GET", url="http://" + item + "." + target, headers=headers, timeout=0.5)
		except requests.exceptions.RequestException:
			pass
	try:
	
		if r != "":
			if "404" not in r:
				print(f"[*] Subdomain Found: {item}.{target}")
				subdoms.append(f"{item}.{target}")
	except UnboundLocalError as e:
		pass
	r = ""
