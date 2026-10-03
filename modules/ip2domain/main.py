import socket
import sys
from colours import RED, GREEN, YELLOW, BLUE, BOLD, RESET

try:
	target = sys.argv[1]
except IndexError:
	target = input(f"{BLUE}Whats the URL your testing? {RESET}")

try:
    hostname, _, _ = socket.gethostbyaddr(target)
    print(f"{GREEN}[*] Host found: {hostname}{RESET}")
except socket.herror:
  print(f"{YELLOW}[*] Scan was unsuccessful{RESET}")
