from selectionSort import sort

def main():	
	shopping_list = {"meat": ["chicken", "beef"], "produce": ["onions", "tomatoes", "jalepenos"], "bread": ["tortillas"], "other": ["laundry detergent"]}
	for key in shopping_list:
		shopping_list[key] = sort(shopping_list[key])
		
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
				shopping_list[cat.lower()] = sort(shopping_list[cat.lower()])
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
	
def getDimensions(dictionary):
	columns = len(dictionary.keys())
	max_rows = 0
	for key in dictionary:
		if len(dictionary[key]) > max_rows:
			max_rows = len(dictionary[key])
	rows = max_rows
	return [rows, columns]
			

def printRow(items, longest, option):
	longest = longest + 3 # Assume a minimum of three spaces.
	if option == "left":
		temp = ""
		for item in items:
			while len(item) < longest:
				item += " "
			temp += item.title()
					
		print(temp)
	elif option == "divider":
		div_length = len(items) * longest
		temp = ""
		while len(temp) < div_length:
			temp += "-"
		print(temp)
			
			

def printTable(list):
	max = getLongest(list)
	print()
	printRow(list.keys(), max, "left")
	printRow(list.keys(), max, "divider")
	dims = getDimensions(list)
	for i in range(dims[0]):
		tempList = []
		for key in list:
			if i < len(list[key]):
				tempList.append(list[key][i].title())
			else:
				tempList.append("")
		printRow(tempList, max, "left")
	print()

		
if __name__ == "__main__":
	main()
		