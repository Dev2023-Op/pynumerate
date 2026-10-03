import whois
import sys
from colours import RED, GREEN, YELLOW, BLUE, BOLD, RESET

def main():
	try:
		target = sys.argv[1]
	except IndexError:
		target = input(f"{BLUE}Whats the target URL? {RESET}")
	try:
		scan = whois.whois(target)
	except whois.exceptions.WhoisError:
		print(f"{YELLOW}[*] Invalid URL")
	try:
		print(GREEN + scan + RESET)
	except UnboundLocalError:
		pass
try:
	main()
except KeyboardInterrupt:
	print()
	print(f"{RESET}exiting")

if __name__ == "__main__":
	try:
		main()
	except KeyboardInterrupt:
		print()
		print(f"{RESET}exiting")
