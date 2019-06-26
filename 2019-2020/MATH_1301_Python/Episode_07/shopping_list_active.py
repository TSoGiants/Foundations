shopping_list = {"meat": ["chicken", "beef"], "produce": ["onions", "tomatoes", "jalepenos"], "bread": ["tortillas"], "other": ["laundry detergent"]}

def getLongest(dictionary):
	longest = 0
	for key in dictionary:
		if len(str(key)) > longest:
			longest = len(str(key))
	for items in dictionary.values():
		for item in items:
			if len(str(item)) > longest:
				longest = len(str(item))
	return longest

def printRow(items, longest):
	longest = longest + 3 # Assume a minimum of three spaces.
	temp = ""
	for item in items:
		while len(item) < longest:
			item += " "
		temp += item.title()
				
	print(temp)

def printTable(list):
	max = getLongest(list)
	print(max)
	printRow(list.keys(), max)
	tempList = []
	for key in list:
		tempList.append(list[key][0].title())
	printRow(tempList, max)
	#	print(key.title() + ":")
	#	for item in list[key]:
	#		print(" * " + item.title())
			
while True:
	text = input("Enter command (read/add/remove/quit): ")
	if(text.lower() == "read"):
		printTable(shopping_list)
	elif(text.lower() == "add"):
		it = input("Enter item name: ")
		print("Current categories:")
		for key in shopping_list:
			print(" * " + key.title())
		cat = input("Which category would you like to add your " + it.lower() + " to? ")
		if cat.lower() in shopping_list.keys():
			shopping_list[cat.lower()].append(it.lower())
		else:
			shopping_list[cat] = [it.lower()]
	elif (text.lower() == "remove"):
		it = input("Enter item to remove: ")
		### This was my fix to the issue of removing an empty key from a dict:
		empties = []	# Create an empty list to store keys that have become empty.
		for key in shopping_list:
			if it.lower() in shopping_list[key]:
				shopping_list[key].remove(it.lower())
				print("Removed " + it + " from category " + key + ".")
				if not shopping_list[key]:	# i.e. If the key is empty.
					empties.append(key)	# Add the key to the list of empty keys.
		for key in empties:		# Go through each key that has been flagged as empty.
			shopping_list.pop(key)	# Take out the trash (remove empty keys).
	
	elif (text.lower() == "quit" or text.lower() == "q"):
		print("Goodbye.")
		break
	else:
		print("I'm sorry, I didn't understand you.")
		