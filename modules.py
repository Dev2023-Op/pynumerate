import os
import sys
import runpy
from colours import RED, GREEN, YELLOW, BLUE, BOLD, RESET

def help(module):
	dir = os.path.dirname(os.path.abspath(__file__))
	err = True
	try:
		with open(f"{dir}/modules/{module}/help", "r") as file:
			page = file.read().splitlines()
			for item in page:
				print(item)
	except FileNotFoundError:
		try:
			with open(f"{dir}/modules/{module}/main.py", "r") as file:
				print(f"{RED}[*] The module specified does not have a help page{RESET}")
		except FileNotFoundError:
			print(f"{RED}[*] Module not found{RESET}")

def list():
	items = os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/modules/")
	for item in items:
		print(item)

if __name__ == "__main__":
    help()
