import whois
import sys

def main():
	try:
		target = sys.argv[1]
	except IndexError:
		target = input("Whats the target URL? ")
	try:
		scan = whois.whois(target)
	except whois.exceptions.WhoisError:
		print("Invalid URL")
	print(scan)

main()

if __name__ == "__main__":
	main()
