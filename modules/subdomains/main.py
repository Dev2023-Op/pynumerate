import sys
import requests
from colours import RED, GREEN, YELLOW, BLUE, BOLD, RESET

subdoms = []

try:
	target = sys.argv[1]
except IndexError:
	target = input(f"{BLUE}Whats the URL your testing? {RESET}")
try:
	try:
		with open("modules/basic/subdomains.txt", "r") as file:
			wordlist = file.read().splitlines()
	except FileNotFoundError:
		try:
			with open("subdomains.txt", "r") as file:
				wordlist = file.read().splitlines()
		except FileNotFoundError:
			print(f"{YELLOW}[*] subdomains wordlist not found{RESET}")
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
					print(f"{GREEN}[*] Subdomain Found: {item}.{target}{RESET}")
					subdoms.append(f"{item}.{target}")
		except UnboundLocalError as e:
			pass
		r = ""

except KeyboardInterrupt:
	print()
	print("exiting)
