import cmd
import os
import sys
import modules
import runpy

class Console(cmd.Cmd):
	prompt = "(pynumerate)> "
	
	def do_exit(self, arg):
		print("\nExiting")
		exit()
	
	def do_basic(self, arg):
		sys.argv = [script, arg]
		original_args = sys.argv
		script = "modules/basic/main.py"
		sys.argv = original_args
		
		runpy.run_path(script)
	
	def do_modules(self, arg):
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
					print("You are missing opptions. enter help if you need it")
			finally:
				sys.argv = original_args
		elif args[0] == "list":
			modules.list()
		elif args[0] == "help":
			modules.help()
		else:
			modules.list()
		
if __name__ == '__main__':
	Console().cmdloop()
