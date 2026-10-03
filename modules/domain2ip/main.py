import socket
import sys
from colours import RED, GREEN, YELLOW, BLUE, BOLD, RESET

try:
	target = sys.argv[1]
except IndexError:
	target = input(f"{BLUE}Whats the URL your testing? {RESET}")

try:
  ip = socket.gethostbyname(target)
  print(f"{GREEN}[*] IP found: {ip}{RESET}")
  info = socket.getaddrinfo(target, 0)
  for item in info:
    print(f"{GREEN}[*] IP found: {ip}{RESET}")
except socket.gaierror:
  print(f"{YELLOW}[*] Scan was unsuccessful{RESET}")
