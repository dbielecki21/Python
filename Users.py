class Users(object):
	def __init__(self, first_name, last_name, age, hair_color):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.hair_color = hair_color
		#self.login_attempts = login_attempts

	def describe_user(self):
		print(self.first_name + " is your first name, you have " + self.hair_color + " hair and you are " + str(self.age))


	def greet_user(self):
		print("Hello " + self.first_name.title() + " how are you?")

	def increment_login_attempts(self, login_attempts):
		login_attempts += 1
		print("The number of attempted logins are: " + str(login_attempts))
		return login_attempts

	def reset_login_attempts(self, login_attempts):
		login_attempts = 0
		print("The number of login attempts has been reset to " + str(login_attempts))

class Admin(Users):
	def __init__(self, first_name, last_name, age, hair_color):
		super(Admin, self).__init__(first_name, last_name, age, hair_color)
		self.privileges = Privileges()

class Privileges(object):
	def __init__(self, privileges=[]):
		self.privileges = privileges

	def show_privileges(self):
		print("\nAdmin Privileges:")
		if self.privileges:
			for privilege in self.privileges:
				print("- " + privilege)
		else:
			print("- this user has no privileges")


		"""for privilege in self.privileges:
			print("- " + privilege)"""

login_attempts = 3
friend_1 = Admin('jared', 'posey', 23, 'black')
friend_1.describe_user()



friend_1.greet_user()
friend_1.increment_login_attempts(login_attempts)
friend_1.reset_login_attempts(login_attempts)

friend_1.privileges.show_privileges()

print("\nAdding privileges....")

friend_1_privileges = [
	'can reset passwords',
	'can moderate discussions',
	'can suspend accounts'
]
print(" ")
friend_1.privileges.privileges = friend_1_privileges
friend_1.privileges.show_privileges()
print(" ")





