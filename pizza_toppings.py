prompt = "\nWhat toppings would you like on your pizza? "
prompt += "\nPlease type 'quit' when you are finished "

while True:
	toppings = input(prompt)

	if toppings == 'quit':
		break
	else:
		print(toppings.title() + " will be added to the pizza")