from numpy import random
import string

letters = string.ascii_lowercase

words = []
with open("word_list.txt", "r") as f:
	word_list = f.read()
	word_list = word_list.split()
	for word in word_list:
		if len(word) > 3 and len(word) < 9:
			words.append(word)
n = random.randint(len(words))
word = words[n]
print(word)

guess = input("What is your guess? ").lower()
if len(guess) == 1 and guess in letters:
	if guess in word:
		indices = []
		for i in range(len(word)):
			if guess == word[i]:
				indices.append(i)
		print("Found your letter at locations: " + str(indices))
	else:
		print("not match")
else:
	print("not ok")
	

