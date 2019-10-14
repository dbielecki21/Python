prompt = "\nPlease enter the name of a city you have visted:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
	city = input(prompt)

	if city =='quit':
		break
	else:
		print("I'd love to go to the " + city.title() + "!")