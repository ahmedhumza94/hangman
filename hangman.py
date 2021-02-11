__author__ = 'humza'

"""
This script plays a command line version of hangman.
Steps:
	1. Initialize game:
		* Choose a random word with the random words package
		* Initialize the number of wrong attempts (default of 6)
	2. Read input from user:
		* Check if the input is an alphabetical character
		* Allow guessing of an entire word to skip to the end of the game
	3. Find index of input character in secret word
	4. If character was not found increment the number of wrong attempts.
		If the character was found update the current progress of user.
        6. Repeat 2-4 until no missing letters in secret word or no more guesses remaining.
	7. Print relevant end of game message
"""

from random_words import RandomWords

def get_word():
	"""
	Select and return a secret word from the random words package.
	"""
	rw = RandomWords()
	selected_word = rw.random_word()
	return selected_word

def read_letter():
	"""
	Get input from command line.
	Output:
		1. Alphabetical String
		2. Boolean flag describing users intention to skip to the end of the game.
	"""
	letter = input("Enter a guess: ")
	skipToEnd = False
	while True:
		#Keep asking for input if it was not an alphabetical str
		try:
			if not letter.isalpha():
				raise ValueError()
		except ValueError:
			letter = input("Enter atleast 1 alphabetical character: ")
			continue

		if len(letter) >1:
			confirm=""
			#Confirm game shortcut with user
			while (confirm != "y") or (confirm != "n"):
				confirm = input("Use {} as guess for final word (y/n): ".format(letter))
				if "y" == confirm:
					skipToEnd = True
					break
				elif "n" == confirm:
					letter = input("Enter atleast 1 chracter: ")
					break
			if skipToEnd == True:
				break
		else:
			#If only 1 letter was entered exit out of the input loop
			break
	return (letter,skipToEnd)

def check_guess(letter,secret_word):
	"""
	Return a list of numeric indices where input letter is found in secret word.
	"""
	#Convert guessed letter and secret word to lower case
	letter = letter.lower()
	secret_word = secret_word.lower()
	#FInd indices of letter in secret word
	idx = [i for i, char in enumerate(secret_word) if letter == char]
	return idx

def play_game(n_guess):
	"""
	Main game loop. Game prints current progress at each iteration.
	"""
	#Ensure n_guess is an integer otherwise
	#use a default of 6 tries
	try:
		n_guess = int(n_guess)
	except ValueError:
		n_guess = 6
	#Choose secret word
	secret_word = get_word()
	print("The secret word has {} letters".format(len(secret_word)))
	#Create list from string for displaying correct guesses
	guessed_string = list("_"*len(secret_word))
	#Create list containing number of wrong guesses
	wrong_guesses = list("_"*n_guess)
	#Initialize number of wrong guesses to 0
	n_wrong = 0
	#Run game loop until word is guessed or enough wrong guesses are made
	while ("_" in "".join(guessed_string)) and (n_wrong < n_guess):
		#Get user guess
		letter, skipToEnd = read_letter()
		if skipToEnd == True:
			guessed_string = list(letter) 
			break
		#Check if guess is in secret word
		idx = check_guess(letter,secret_word)
		#Check if no match was found
		if not idx:
			#Update number of wrong guesses
			wrong_guesses[n_wrong] = "X"
			n_wrong += 1
		else:
			#Edit current progress
			for i in idx:
				guessed_string[i] = secret_word[i]
		#Print current progress as a string
		print("Current Progress: {}".format("".join(guessed_string)))
		#Print number of wrong tries
		print("Wrong Guesses: {}\n".format("".join(wrong_guesses)))

	#Check if user won or ran out of tries
	if ("".join(guessed_string) == secret_word) and (n_wrong < n_guess):
		print("You win!")
	else:
		print("Game over")
		print("The secret word was {}".format(secret_word))

def main():
	play_game(n_guess=6)

if __name__ == "__main__":
	main()
