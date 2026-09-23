import os
import sys
import runpy

def help():
	print("help: show this list")
	print("list: lists the installed modules")
	print("use:  use a module")
	print()
	print("If i wanted to run a basic scan on example.target i would run modules use basic example.target")

def list():
	items = os.listdir("modules/")
	for item in items:
		print(item)

if __name__ == "__main__":
    help()
