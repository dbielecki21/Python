# start with some design that needs to be printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

#Simulate printing each design, until none are left
#Move each design to completed_models after priting
while unprinted_designs:
	current_design = unprinted_designs.pop()

	#Simulating creating a 3D print from the design
	print("Printing model:" + current_design)
	completed_models.append(current_design)

#Display all completed models
print("\nThe following models have been printed:")
for completed_models in completed_models:
	print(completed_models)