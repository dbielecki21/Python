sandwhich_orders = ['ham', 'pastrami', 'chicken', 'pastrami', 'salami', 'pastrami', 'turkey']
finished_sandwhiches = []
print(sandwhich_orders)
print("\nThe deli has run out of pastrami ")

while 'pastrami' in sandwhich_orders:
	sandwhich_orders.remove('pastrami')

while sandwhich_orders:
	current_sandwhich = sandwhich_orders.pop()
	print("I'm working on your " + current_sandwhich + " sandwhich. ")
	finished_sandwhiches.append(current_sandwhich)

print("\n")
for sandwhich in finished_sandwhiches:
	print("I made a " + sandwhich + " sandwhich.")