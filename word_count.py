def count_words(filename):
	#count the approximate number of words in a file
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sorry, the file " + filename + " does not exist"
		print(msg)
	else:
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filename = ['alice.txt', 'moby_dick.txt']
for filename in filename:
	count_words(filename)