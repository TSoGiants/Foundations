shopping_list = {"meat": ["chicken", "beef"], "produce": ["onions", "tomatoes", "jalepenos"], "bread": ["tortillas"], "other": ["laundry detergent"]}

while True:
	text = input("Enter command (read/add/remove/quit): ")
	if(text.lower() == "read"):
		for key in shopping_list:
			if(shopping_list[key]):		### This is a kludgy workaround.
										### I will fix this when I figure out the
										### best way to remove empty keys from a dict.
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
		for key in shopping_list:
			if it.lower() in shopping_list[key]:
				shopping_list[key].remove(it.lower())
				print("Removed " + it + " from category " + key + ".")
		#########################################################################
		### This is probably where we should remove the empty keys from list. ###
		#########################################################################
	elif (text.lower() == "quit" or text.lower() == "q"):
		print("Goodbye.")
		break
	else:
		print("I'm sorry, I didn't understand you.")
		