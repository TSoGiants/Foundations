shopping_list = {"meat": ["chicken", "beef"], "produce": ["onions", "tomatoes", "jalepenos"], "bread": ["tortillas"], "other": ["laundry detergent"]}

for key in shopping_list:
	print(key.title() + ":")
	for item in shopping_list[key]:
		print(" * " + item.title())