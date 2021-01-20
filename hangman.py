from random_words import RandomWords

def get_word():
	rw = RandomWords()
	selected_word = rw.random_word()
	return selected_word

def read_letter():
	letter = input("Enter a guess: ")
	skipToEnd = False
	while True:
		if len(letter) == 0:
			letter = input("Enter atleast 1 chracter: ")
		elif len(letter) >1:
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
			break
	return (letter,skipToEnd)

def check_guess(letter,secret_word):
	#Convert guessed letter and secret word to lower case
	letter = letter.lower()
	secret_word = secret_word.lower()
	idx = [i for i, char in enumerate(secret_word) if letter == char]
	return idx

def play_game(n_guess):
	#Ensure n_guess is an integer
	n_guess = int(n_guess)
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
		#Print number of wrong tires
		print("Wrong Guesses: {}\n".format("".join(wrong_guesses)))

	#Check if user won or ran out of tries
	if ("".join(guessed_string) == secret_word) and (n_wrong < n_guess):
		print("You win!")
	else:
		print("Game over")
		print("The secret word was {}".format(secret_word))

def main():
	play_game(6)

if __name__ == "__main__":
	main()
