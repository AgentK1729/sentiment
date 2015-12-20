from re import match
from sqlite3 import connect

# Regexes for hyperlinks, numbers, hastags and handles
patterns = [r'http://([a-zA-z0-9]+/*)+[.][a-zA-z]+', r'[0-9]+([.][0-9]+)*', r'#[a-zA-z0-9]+', r'@[a-zA-z0-9]+',
r'[a-z]+ing', r'[a-z]+ed']
puctuations = ".,/?!'#$%^&*()@[]{}:;"

def Filter (tweet):
	tweet = tweet.split (" ")
	filtered = []
	# Remove hyperlinks, numbers, hastags and handles
	for word in tweet:
		word = word.lower ()
		count = 0
		for i in range (len (patterns)):
			try:
				match (patterns[i], word).group ()
				# Take care of tense
				if i == 4:
					word = word[0:-3]
					filtered.append (word)
					break
				elif i == 5:
					word = word[0:-2]
					filtered.append (word)

			except AttributeError:
				count += 1

		if count == 6:
			filtered.append (word)

	# Remove puctuations
	temp = []
	for word in filtered:
		final = ""
		for char in word:
			if char not in puctuations:
				final += char
		temp.append (final)

	filtered = temp


	return filtered

"""
@PC_Hard_Drives: Reliable and practical 
#data #storage with #Toshiba #Canvio 3.0 1.5 TB; 
Unmissable offer! http://t.co/zGUzx8Xe7
"""
#print Filter ("Killed Killing kill eating eat")

