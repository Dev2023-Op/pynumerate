import sys
import subprocess
from colours import RED, GREEN, YELLOW, BLUE, BOLD, RESET

buckets = []

try:
	target = sys.argv[1]
except IndexError:
	target = input(f"{BLUE}Whats the URL your testing? {RESET}")

try:
	cmd = "aws s3 ls s3://" + target + " --no-sign-request"
	result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
	if "ERROR" not in result.stdout and "ERROR" not in result.stderr:
		print(f"{GREEN}[*] S3 bucket found: s3://{target}{RESET}")
except KeyboardInterrupt:
	print()
	print(f"{RESET}exiting")
