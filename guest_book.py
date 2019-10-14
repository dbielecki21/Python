filename = 'guest_book.txt'

print("Enter 'quit' when you are finished")
while True:
	name = raw_input("\nWhat's your name? ")
	if name == 'quit':
		break
	else:
		with open(filename, 'a') as f:
			f.write(name + "\n")
		print("Hi " + name + ", you've been added to the guest book")