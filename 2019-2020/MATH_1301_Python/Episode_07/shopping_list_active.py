shopping_list = {"meat": ["chicken", "beef"], "produce": ["onions", "tomatoes", "jalepenos"], "bread": ["tortillas"], "other": ["laundry detergent"]}

while True:
	text = input("Enter command (read/add/remove/quit): ")
	if(text.lower() == "read"):
		for key in shopping_list:
			print(key.title() + ":")
			for item in shopping_list[key]:
				print(" * " + item.title())
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
		