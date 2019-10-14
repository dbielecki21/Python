class Car(object):
	def __init__(self, make, model, year):
		"""Initialize attributes to describe a car"""
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		"""return a neatly formateed descriptive name."""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def update_odometer(self, milages):
		"""set the odometer reading to the given value.
		Reject the change if it attempts to roll the odometer back
		"""
		if mileage > self.odometer_reading:
			self.odometer_reading += mileage
		else:
			print("you cant roll back an odometer")

	def increment_odometer(self, miles):
		"""Add the given amount to the odometer reading.""" 
		self.odometer_reading += miles

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

class Battery():
	def __init__(self, battery_size):
		#initialize the batter's attributes
		self.battery_size = battery_size

	def describe_battery(self):
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

	def get_range(self):
		#print a statement about the range of this battery provides
		if self.battery_size == 70:
			range = 240
			message = "This car can go approximately " + str(range)
			message += " miles on a full charge"
		elif self.battery_size == 85:
			range = 270
			message = "This car can go approximately " + str(range)
			message += " miles on a full charge after the battery upgrade"
		print(message)

	def upgrade_battery(self):
		if self.battery_size < 85:
			self.battery_size = 85
		elif self.battery_size > 85:
			self.battery_size = 85
		else:
			self.battery_size = 85
		return(self.battery_size)

class ElectricCar(Car):
	#represents aspects fo a car, specific to electric vehicles
	def __init__(self, make, model, year):
		super(ElectricCar, self).__init__(make, model, year)
		battery_size = 70
		self.battery = Battery(battery_size)

	'''def describe_battery(self):
		#print a statement describing the battery size
		print("This car has a " + str(self.battery_size) + "-kWh battery.")'''

	def fill_gas_tank(self):
		"""electric cards dont't have gas tanks."""
		print("This car doesn't have a gas tank")

#battery_size = 70
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()

print(" ")

my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()

print(" ")

my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.increment_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
print(" ")