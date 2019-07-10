words = []
with open("word_list.txt", "r") as f:
	word_list = f.read()
	word_list = word_list.split()
	print(len(word_list))
	for word in word_list:
		if len(word) > 3 and len(word) < 9:
			words.append(word)
#print(words)
print(len(words)) # Temporary
