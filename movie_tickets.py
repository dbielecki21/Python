prompt = "\nHow old are you? "
prompt += "\nEnter 'quit' when done "

while True:
	age = input(prompt)

	if age == 'quit':
		break
	elif int(age) < 3:
		print("That ticket will be free")
	elif (int(age) >= 3) & (int(age) <= 12):
		print("That ticket will be $10")
	elif int(age) > 12:
		print("That ticket will be $15"),