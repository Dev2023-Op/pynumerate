import sys
import subprocess

buckets = []

try:
	target = sys.argv[1]
except IndexError:
	target = input("Whats the URL your testing? ")

try:
	cmd = "aws s3 ls s3://" + target + " --no-sign-request"
	result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
	if "ERROR" not in result.stdout and "ERROR" not in result.stderr:
		print(f"[*] S3 bucket found: s3://{target}")
except KeyboardInterrupt:
	print()
	print("exiting")
