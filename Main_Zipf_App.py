from Get_Words import returnSpanishDict
from Get_Words import generatespanishWord
import pandas


'''
Ok so this application asks users to translate Spanish words.  There are two modes, easy and hard.  In easy mode, the first time a user
gets a word correct, it increases his score.  In hard mode, the user must get 5 answers correct.  In the future, I will make it so that in
hard mode the user needs to get 5 consecutive words correct, but that is unimplemented.  The way it works is that in Spanish, when people speak or 
write, usually the thousand most common words make up like, 60% of what is said.  So I used the first thousand words and as users learn them, they will
get closer and closer to that 60%.  Hopefully the rest is understandable.
'''


def update_word_score(SpanishDict, spanishword, correct):
	if correct:
		SpanishDict[spanishword][2] += 1  		# Update correct score
		SpanishDict[spanishword][3] += 1		# Update total count score
	else:
		SpanishDict[spanishword][3] += 1 		# Only update total count score
	return SpanishDict[spanishword][2]

# print("Testing update_word_score")
# print(update_word_score(dummy_Spanish_Word[1], True))
		
def convert_to_percentage(number):  			# This is used for printing out a user's score.  It converts a number to a percentage with 2 trailing digits 
	percentage = str(number)
	if number > 10:
		return percentage[:5] + "%"
	else:
		return percentage[:4] + "%"
		
# print("Testing convert_to_percentage")

# print(convert_to_percentage(12.8495902203))
		
def zipf_Score_Calculator(spanishword, currentscore, denominator):  			# This uses the Zipf equation to calculate a user's updated score
	numberSpanishWords = 125000 		# This is a rough estimate of the total number of Spanish words, which is necessary for Zipf's equation
	currentscore += 1/(int(spanishword[0])*denominator)
	return currentscore 

# print("Testing Zipf Score Calculator")

# print(zipf_Score_Calculator(dummy_Spanish_Word, 0, 12.3))

	
def full_Zipf_App():
	SpanishDict = returnSpanishDict() 			# Grab the spanish dict from get_words.py
	currentScore = 0 							# starting score is at 0
	keepPlaying = True							# This is necessary for the while Loop
	askToQuitCount = 1 							# This is for checking if a user wants to quit

	
	denominator = 0
	for number in range(1,125000):  			# We need to calculate a Harmonic Series based off the number of words in Spanish (roughly 125000)
		denominator += 1/number 				# This code is just for calculating part of the zipf equation.  It was kept out of the Zipf calculator because I didn't want to run the loop every time
	print("Welcome to the Zipf flashcard game! \nThis game will attempt to calculate how well you know common Spanish vocab \
			\nThanks for playing!  Your current score is 0%.  Let's get it higher!  		\
			\nIf you want to quit at any time, simply type 'q' and hit enter!")
	
	
	while True:  								# This is a loop that keeps asking the user if he wants easy or hard mode
		modechoice = input("First tell us if you would like to play on Easy Mode or Hard Mode by typing 'easy' or 'hard':   ")
		if modechoice == "easy":
			easymode = True
			break
		elif modechoice == "hard":
			easymode = False
			break
		else:
			print("Sorry, you need to type either 'easy' or 'hard'")
		
	
	
	
	while keepPlaying: 							# The app uses a while loop to keep asking a user if he/she wants to play
		
		spanishWord = generatespanishWord()	 	# This is from get_words.py, it returns a tuple with a randomly selected Spanish word, the english translation and the rank
		print("Your word is " + spanishWord[1])
		answer = input("What is the English Translation? ")
		
		
		if answer == "q" or answer == "Q": 		# The player can quit at any time by typing "q" or "Q"
			keepPlaying = False
		
		if easymode: 							# Easy mode means that the first time a user gets a word correct, his/her score is updated
			if answer == spanishWord[2]: 		
				update_word_score(SpanishDict, spanishWord[1], True)
				if SpanishDict[spanishWord[1]][2] == 1:	 			# We don't want to double count a correct word, so only when word_score hits 1 do we update a user's score
					currentScore = zipf_Score_Calculator(spanishWord[0], currentScore, denominator)
				print("Great job! You increased your score!  Now it is " + convert_to_percentage(currentScore))
			else:
				correct = False 									# Here, we just update how many times the user has received a word.  I will make a newer edition where this is used
				update_word_score(SpanishDict,spanishWord[1], False)
				print("Shoot, that wasn't correct! The correct translation was '" + spanishWord[2] + "'. \
				\nYour score is still " + convert_to_percentage(currentScore))
			
			
		else:
			if answer == spanishWord[2]: 							# This is hard mode.  A user needs to get a score over 4 before his/her total score is updated
				if SpanishDict[spanishWord[1]][2] > 4:
					update_word_score(SpanishDict, spanishWord[1], True)
					if SpanishDict[spanishWord[1]][2] == 5: 		# this checks if the score is at 5, so we can increase the user's total score
						currentScore = zipf_Score_Calculator(spanishWord[0], currentScore, denominator)
					print("Great job! You increased your score!  Now it is " + convert_to_percentage(currentScore))
				else:
					update_word_score(SpanishDict, spanishWord[1], True)
					print("Correct! Your score is " + convert_to_percentage(currentScore)) 			# If the 
			else:
				correct = False	 									# If the answer is wrong, we just update the word_count for that word
				update_word_score(SpanishDict, spanishWord[1], False)
				print("Shoot, that wasn't correct! The correct translation was '" + spanishWord[2] + "'. 		\
				\nYour score is still " + convert_to_percentage(currentScore))
			
			
		if askToQuitCount % 10 == 0: 								# Here is a loop that asks the user if he wants to quit every 10 words
			while True:
				play = input("Would you like to keep playing?(y/n)")
				if play == "y" or play == "Y":
					keepPlaying = True
					break
				elif play == "n" or play == "N":
					keepPlaying = False
					break
				else:
					print("Can you try answering again?  I only take y or n")
		
		askToQuitCount += 1
		
	print("Thanks for playing! Your final score was " + convert_to_percentage(currentScore))
	return
		
		
	
	
full_Zipf_App()
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
