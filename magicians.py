def show_magicians(magicians):
	#Print the name of each magician in the list
	for magician in magicians:
		print(magician)

def make_great(magicians):
	great_magicians = []

	#make each magician great, and add it to great_magicians
	while magicians:
		magician = magicians.pop()
		great_magician = magician + ' the Great'
		great_magicians.append(great_magician)

	# add teh great magician back into magicians
	for great_magician in great_magicians:
		magicians.append(great_magician)

magicians = ['harry houdini', 'david blaine', 'teller']
show_magicians(magicians)

print("\nGreat magicians:")
great_magicians = make_great(magicians[:])
show_magicians(magicians)

print("\nOriginal magicians:")
show_magicians(magicians)