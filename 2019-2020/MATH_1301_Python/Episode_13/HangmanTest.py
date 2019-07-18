from HangmanObj import Hangman

game = Hangman()

while not game.game_won and not game.game_lost:
	print(game)
	while True: # Input loop.
		result = game.makeGuess(input("What is your guess? "))
		print(result[1]) # Print whatever string Hangman.makeGuess() returns.
		if result[0]:
			break
	
print(game)