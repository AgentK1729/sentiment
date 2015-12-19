# -*- coding: utf-8 -*-
from sqlite3 import connect

class Word (object):
	def __init__ (self, word, scores):
		self.word = word
		self.scores = scores

	def __str__ (self):
		scores = ""
		for score in self.scores:
			scores += str (score) + " "
		return self.word + ": " + scores

def getScores (word):  # Take a word and return a Word object
	newWord = Word (word, [])
	conn = connect ("wordlist.db")
	cur = conn.cursor ()

	query = "select * from word where word = ?"
	cur.execute (query, (word,))
	for row in cur:
		newWord.scores.append (row[1]-row[2])

	conn.close ()
	if len (newWord.scores) == 0:
		newWord.scores.append (0.0)
	return newWord



def getSentiment (sentence):
	final_scores = []
	words = []
	sentence = sentence.split(" ")
	for word in sentence:
		words.append(getScores(word))

	if len (words) == 1:
		return words[0].scores[0]

	else:
		# First two words
		Min = 9999
		best = (0, 0)
		for i in words[0].scores:
			for j in words[1].scores:
				diff = abs (i-j)
				if diff < Min:
					best = (i, j)
					Min = diff

		final_scores.append (best[0])
		final_scores.append (best[1])

		# Rest of the words
		for i in words[2:]:
			score = final_scores[-1]
			Min = 9999
			for j in i.scores:
				if abs (score-j) < Min:
					Min = j
			final_scores.append (j)

		sentiment = 0
		for i in final_scores:
			sentiment += i
		return sentiment