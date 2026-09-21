import cmd
import os
import sys
import modules

class Console(cmd.Cmd):
	prompt = "(pynumerate)> "
	
	def do_exit(self, arg):
		print("\nExiting")
		exit()

if __name__ == '__main__':
	Console().cmdloop()
