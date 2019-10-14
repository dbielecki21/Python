
file = open("Devices.txt", "r")

for line in file:
	line1 = line.rstrip('\n')
	domain = line1.split()
	if (len(domain) == 1):
		domain.append(None)
	device_parts = [domain[0], "uberboss", "ChangeMe!", domain[1]]
	machines.append(device_parts)

file.close()
print (machines)

