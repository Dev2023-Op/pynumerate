import cmd
import os
import sys
import modules
from colours import RED, GREEN, YELLOW, BLUE, BOLD, RESET
import runpy
import random

def art():
	files = os.listdir(os.path.dirname(os.path.abspath(__file__)) + "/resources/art/")
	choice = os.path.dirname(os.path.abspath(__file__)) + "/resources/art/" + random.choice(files)
	with open(choice, "r") as file:
		print(RED + file.read() + RESET)
	

class Console(cmd.Cmd):
	prompt = f"{GREEN}({RED}pynumerate{GREEN})> {RESET}"
	
	def do_exit(self, arg):
		"""Exit pynumerate"""
		print("\nExiting")
		exit()
	
	def do_modules(self, arg):
		"""Access the module function\nType modules help for more information"""
		args = arg.split()
		
		if args[0] == "use":
			original_args = sys.argv
			try:
				try:
					dir = os.path.dirname(os.path.abspath(__file__))
					script = dir + "/modules/" + args[1] + "/main.py"
					sys.argv = [script]
					i = 0
					for item in args:
						if i == 0 or i == 1:
							i += 1
						else:
							sys.argv.append(item)
					runpy.run_path(script)
				except IndexError:
					print(f"{YELLOW}[*] You are missing opptions. enter help if you need it{RESET}")
			finally:
				sys.argv = original_args
		elif args[0] == "list":
			modules.list()
		elif args[0] == "help":
			modules.help()
		else:
			modules.list()
		
if __name__ == '__main__':
	try:
		art()
		Console().cmdloop()
	except KeyboardInterrupt:
		print()
		print(f"{RESET}exiting")
