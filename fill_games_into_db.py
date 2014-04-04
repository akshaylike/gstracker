import sqlite3
import json

json_file = open('gmggames.json')
list_of_games = json.load(json_file)

conn = sqlite3.connect('development.sqlite3')
query = ""
id = 1
for each in list_of_games:
	try:
		onSale = int(each['onSale'][0])
		#steamworks = int(each['steamworks'][0])
		gameTitle = each['gameTitle'][0]
		gameLink = each['gameLink']
		rrp = float(each['rrp'][0][1:])
		drp = 0
		if onSale == 1:
			drp = float(each['drp'][0][1:])
		query = "INSERT INTO GAMES VALUES(%d, \"%s\", %f, %f, %d, \"%s\")" % (id, gameTitle, rrp, drp, onSale, gameLink) + ";"
		id = id + 1
		
	except IndexError:
		pass

	else:
		#print query
		#print
		pass
		conn.execute(query)

conn.commit()
conn.close()
