from sentiment import Sentiment
from tweets import getTweets

def analyze(term, count):
	tweets = getTweets(term, count)
	return Sentiment(tweets)
