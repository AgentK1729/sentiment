import filter, tweets, sentiment, sys
from sys import argv

if len(argv) == 3:
	# Get search term and count of tweets to be analyzed from command line arguments
	dataset = tweets.getTweets(argv[1], argv[2])

	# Call function to get sentiment
	print sentiment.Sentiment(dataset)

else:
	print "Usage: python main.py <search term> <no. of tweets to analyze>"