class Restaurant(object):

	def __init__(self, name, cusine_type):
		self.name = name
		self.cusine_type = cusine_type
		#self.number_served = 0
	
	def describe_restraurant(self):
		print(self.name.title() + " is the name of the restaurant")
		print(self.cusine_type.title() + " is the type of cusine")

	def open_restaurant(self):
		print(self.name.title() + " is open")

	def set_number_served(self):
		self.number_served = 0
		print("This restraut started the day with " + str(self.number_served) + " customers served")

	def increment_number_served(self, customers):
		self.number_served += customers
		print("This restaurant has now served " + str(self.number_served))

class IceCreamStand(Restaurant):

	def __init__(self, name, cusine_type='ice_cream'):
		super().__init__(name, cusine_type)
		self.flavors = []

	def show_flavors(self):
		print("\nWe now have the following flavors available")
		for flavor in self.flavors:
			print("- " + flavor.title())



'''
restaurant_1 = Restaurant('Pazzos', 'pizza')
restaurant_1.set_number_served()
restaurant_1.increment_number_served(12)'''

big_one = IceCreamStand('The Big One')
big_one.flavors = ['vanila', 'chocolate', 'mint']
big_one.describe_restraurant()
big_one.show_flavors()


"""
restaurant_1 = Restaurant('Pazzos', 'pizza')
restaurant_2 = Restaurant('Hopcat', 'crack fries')

restaurant_1.describe_restraurant()
restaurant_1.open_restaurant()

restaurant_2.describe_restraurant()
restaurant_2.open_restaurant()
print(restaurant_1.describe_restraurant())
print("\n" + restaurant_1.open_restaurant())
"""
