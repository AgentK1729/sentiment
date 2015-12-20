from sqlite3 import connect

conn = connect("wordlist.db")
cur = conn.cursor()

"""query = '''
	create table word
	(
		word varchar(30),
		posscore float(5),
		negscore float(5)
	);'''
"""

f1 = open("sentiments.txt", "r")
for line in f1:
	try:
		essential = line.split("\t")[2:5]
		posscore, negscore = float(essential[0]), float(essential[1])
		for part in essential[-1].split(" "):
			word = part.split("#")[0]
			data = (word, posscore, negscore)
			print data
			cur.execute("insert into word values (?, ?, ?)", data)
			conn.commit()
	except:
		pass
	
f1.close()
conn.commit()
conn.close()