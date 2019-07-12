from numpy import random
import string

def main():
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
	print(word)	# Temporary use only
	progress = []
	for c in word:
		progress.append("_")
	s = parseProgress(progress)
	print("Word to guess: " + s)
	

	guess = input("What is your guess? ").lower()
	if len(guess) == 1 and guess in letters:
		if guess in word:
			indices = []
			for i in range(len(word)):
				if guess == word[i]:
					indices.append(i)
			if len(indices) > 1:
				s = 's.'
			else:
				s = '.'
			print("The word contained " + str(len(indices)) + " " + guess.upper() + s)
			for i in indices:
				progress[i] = guess.upper()
		else:
			print("not match")
	else:
		print("not ok")

	s = parseProgress(progress)
	print(s)
	
	
	
def parseProgress(progress):
	output = ""
	for letter in progress:
		output += letter.upper() + " "
	return output

### printGallows() generates variations on the following feedback diagram:
"""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""
def printGallows(count):
	if isinstance(count, int):
		gameOver = False
		gallows = "      |"
		base = "========="
		### Print first line:
		print("  +---+")
		
		### Print second line:
		print("  |   |")
		
		### Begin third line:
		if count > 0:
			print("  O   |")
		else:
			print(gallows)
			
		### Begin fourth line:
		s = " "
		if count > 3:
			s += "/|\x5C"	# Left arm, torso, and right arm.
							# Note: Have to use hexadecimal code for backslash 
							# because backslash is an escape character.
		elif count > 2:
			s += "/| "	# Left arm and torso.
		elif count > 1:
			s += " | "	# Torso only.
		else:
			s += "   "  # Space for arms and torso but none displayed.
		s += "  |"	# Rest of gallows.
		print(s)
		
		### Begin fifth line:
		s = " "
		if count > 5:
			s += "/ \x5C"	# Left and right leg.
							# Note: Have to use hexadecimal code for backslash 
							# because backslash is an escape character.
			gameOver = True
		elif count > 4:
			s += "/  "	# Left leg only.
		else:
			s += "   "	# Space for legs but none displayed.
		s += "  |"	# Rest of gallows.
		print(s)
		
		### Begin sixth line:
		print(gallows)
		
		### Begin seventh line:
		print(base)
		
		return gameOver
	else:
		print("Function printGallows() can only accept integers.")
		return True

if __name__ == "__main__":
	main()