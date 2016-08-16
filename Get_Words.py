import csv
import random
import os 
import pandas

SpanishDict = {}

cwd = os.getcwd()

csvPath = os.path.join(cwd,"Spanish_Words.csv")

'''
This is all pretty straightforward.  The first function just gets the words from a CSV, the next generates a tuple 
with the rank (important for calculating score), the spanish word and its english equivalent.
The last function just returns that dictionary.
'''

	

with open(csvPath) as wordfile:
	myreader = csv.reader(wordfile)
	for row in myreader:
		SpanishDict[row[1]] = [row[2],row[0], 0, 0]
		#spanish_df.loc[row[0]] = [row[1], row[2], row[0], 0, 0]

def generatespanishWord():
	SpanishWord = random.choice(list(SpanishDict.keys()))
	EnglishWords = SpanishDict[SpanishWord][0]
	rank = SpanishDict[SpanishWord][1]
	return (rank, SpanishWord, EnglishWords)
	
def returnSpanishDict():
	return SpanishDict