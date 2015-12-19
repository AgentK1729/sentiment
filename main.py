import filter, tweets, sentiment, sys
from sys import argv

if len(argv) == 3:
	dataset = tweets.getTweets(argv[1], argv[2])
	senti = 0.0
	for tweet in dataset:
		senti += sentiment.Sentiment(tweet)
	print senti
else:
	print "Usage: python main.py <search term> <no. of tweets to analyze>"