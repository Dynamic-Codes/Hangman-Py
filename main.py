'''
COPYRIGHT DYNAMIC CODES
@GITHUB 2022
ANSH P.
USE ONLY WITH PERMISSION
'''


from os import system as console
from time import sleep as pause

correct  = ''
left     = []
attempts = 0
fails    = 0
maxAttempt = 5

#--------
def Won():
	console('cls')
	print(f'-----------CONGRATS!!\n\nYou have won the game in..\n{attempts} Attemps\nwith\n{fails} wrong guesses!')
	pause(5)
	exit('Program ended.')

def Display():
	answer = ''
	for letter in correct:
		if letter in left:
			answer += ' _ '
		else:
			answer += letter
	return answer

def Check(guess):
	global correct
	global left
	global attempts
	global fails

	if (len(guess)) == 0:
		print('[!] Please enter something..')
		pause(2)
		return False
	elif len(guess) == 1:
		attempts += 1
		if guess in left:
			print('[i] Letter in word!')
			left.remove(guess)
			pause(1)
		else:
			print('[!] Letter not found.')
			fails += 1
			pause(2)

		if (len(left)) == 0:
			return True
		else:
			return False
	else:
		if guess == correct:
			return True
		else:
			print('[!] Incorrect word..')
			pause(2)
			return False


def GameSettings():
	global correct
	global left

	print('----Welcome\n\nTo start hangman, please complete the setup below.\n')
	correct = input('Secret Phrase: ')
	for letter in correct:
		left.append(letter)

while True:
	console('cls')
	if correct == '':
		GameSettings()
	print(Display())
	wpGuess = input('Guess a letter or phrase: ')
	val = Check(wpGuess)
	if val is True:
		Won()
		break