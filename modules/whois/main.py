import whois

try:
	target = sys.argv[1]
except IndexError:
	target = input("Whats the target URL? ")

scan = whois.whois(target)

if __name__ == "__main__":
	main()
