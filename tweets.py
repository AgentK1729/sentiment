import tweepy
from sqlite3 import connect, IntegrityError
from time import sleep

class Tweet (object):
	def __init__ (self, id, text):
		self.id = id
		self.text = text

# Tweepy status object structure
"""
{
 'contributors': None,
 'truncated': False,
 'text': 'My Top Followers in 2010: @tkang1 @serin23 @uhrunland @aliassculptor @kor0307 @yunki62. Find yours @ http://mytopfollowersin2010.com',
 'in_reply_to_status_id': None,
 'id': 21041793667694593,
 '_api': <tweepy.api.api object="" at="" 0x6bebc50="">,
 'author': <tweepy.models.user object="" at="" 0x6c16610="">,
 'retweeted': False,
 'coordinates': None,
 'source': 'My Top Followers in 2010',
 'in_reply_to_screen_name': None,
 'id_str': '21041793667694593',
 'retweet_count': 0,
 'in_reply_to_user_id': None,
 'favorited': False,
 'retweeted_status': <tweepy.models.status object="" at="" 0xb2b5190="">,
 'source_url': 'http://mytopfollowersin2010.com',
 'user': <tweepy.models.user object="" at="" 0x6c16610="">,
 'geo': None,
 'in_reply_to_user_id_str': None,
 'created_at': datetime.datetime(2011, 1, 1, 3, 15, 29),
 'in_reply_to_status_id_str': None,
 'place': None
}
</tweepy.models.user></tweepy.models.status></tweepy.models.user></tweepy.api.api>
"""


def getTweets (term, total):
    conn = connect ("sentiment.db")
    cur = conn.cursor ()
    last_id = ""
    try:
        cur.execute ("select last_id from analysis_company where name = ?", (term,))
        for row in cur:
            last_id = row[0]
    except IntegrityError:
        pass

    consumer_key = "uliyBZTVSySlodxPDjtcyNtPu"
    consumer_secret = "MpCKyNkGf0QLHaWfKwlT0cRhM7ePgiBw0EkddOKVycyLmJvu1N"
    access_token = "2709554664-0sBHVIbNIoSKfmjikdWXrFSUIn0JFEtTFzkCnMU"
    access_token_secret = "lJTVhCj2eUS8x5Po8dA0wzPNx0NE1LkXEhWWpwvBZyDrc"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    # Creation of the actual interface, using authentication
    # api = tweepy.API(auth, proxy_url="proxy.server:3128")
    api = tweepy.API(auth)
    count = 0
    c = tweepy.Cursor(api.search, q = term, lang = 'en')
    tweets = []
    for tweet in c.items():
    	try:
    		if count > total:
    			break
    		else:
    			tweets.append (Tweet (str(tweet.id), tweet.text))
    			count += 1
    	except tweepy.error.TweepError:
    		sleep(1)
    		continue
    conn.close ()
    return tweets
