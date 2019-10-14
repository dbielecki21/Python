name = input("Whats your name? ")

filename = 'guests.txt'

with open(filename, 'w') as f:
	f.write(name)