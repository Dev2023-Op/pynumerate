import requests
import sys
from colours import RED, GREEN, YELLOW, BLUE, BOLD, RESET

r = ""
content = ""

try:
	target = sys.argv[1]
except IndexError:
	target = input(f"{BLUE}Whats the URL your testing? {RESET}")

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/152.0.0.0 Safari/537.36"
}

def wp():
    global content
    if "w.org" in content:
        print(f"{GREEN}[*] The target is likely WordPress{RESET}")

def drupal():
    global content
    if "(https://www.drupal.org)" in content:
        print(f"{GREEN}[*] The target is using Drupal{RESET}")

def yoast():
    global content
    if "This site is optimized with the Yoast SEO plugin" in content:
        print(f"{GREEN}[*] The target is using Yoast SEO{RESET}")

def joomla():
    global r
    try:
        if "Joomla" in r.headers["X-Content-Encoded-By"]:
            print(f"{GREEN}[*] The target is using Joomla{RESET}")
    except KeyError:
        pass

def gtm():
    global content
    if "https://www.googletagmanager.com/gtm.js" in content:
        print(f"{GREEN}[*] The target is using Google Tag Manager{RESET}")

def main():
    global headers
    global target
    global r
    global content
    
    if "http://" not in target.lower() and "https://" not in target.lower():
        if input("HTTP or HTTPS?").lower() == "http":
            target = "http://" + target
        elif input("HTTP or HTTPS?").lower() == "https":
            target = "https://" + target
        else:
            print("invalid input")
            exit()

    try:
        r = requests.request("GET", target, headers=headers, timeout=5)
    except ReadTimeout:
        print(f"{RED}[*] Target timed out{RESET}")
        exit()
    else:
        content = r.text

    try:
        print(f"{GREEN}[*] The target is powered by {r.headers['X-Powered-By']}")
    except KeyError:
        pass
            
    wp()
    drupal()
    yoast()
    joomla()
    gtm()
try:
	main()
except KeyboardInterrupt:
	print()
	print("exiting")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print()
		print("exiting")
	exit()