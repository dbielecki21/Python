#names = ['admin','david','charles', 'rob', 'tony', 'jeffry']
names = []
#requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

if names != []:
	for name in names:
		if name == "admin":
			print("Hello " + name + " would you like to see a status report? ")
		else:
			print("Hello " + name + " thank you for logging in again ")
else:
	print("We need to find some users")

#print("\nFinished making your pizza!")
