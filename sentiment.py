from successive import *
from filter import Filter
import threading

global sentiment
sentiment = 0.0

class sentimentThread (threading.Thread):
	def __init__ (self, tweets):
		threading.Thread.__init__(self)
		self.tweets = tweets

	def run (self):
		global sentiment
		for tweet in self.tweets:
			temp = Filter (tweet.text)
			words = []
			for word in temp:
				words.append (getScores (word))
			sentiment += getSentiment (words)


def Sentiment (tweets):
	global sentiment
	threads = []
	temp = int(len(tweets)/5)
	for i in range (5):
		threads.append (sentimentThread (tweets[(0+i*temp):(temp+i*temp)]))

	for thread in threads:
		thread.start ()


	for thread in threads:
		thread.join ()

	return sentiment
