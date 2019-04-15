# ==================================================
# Written in March 2016 by Victoria Anugrah Lestari
# ==================================================
import json

# ==================================================
# Membaca dictionary dari json
# ==================================================
def load(filename):	
	with open(filename) as data_file:
		data = json.load(data_file)	

	return data

# load dictionary
mydict = load('dict.json')

# ==================================================
# Mencari sinonim suatu kata
# ==================================================
def getSinonim(word):
	sinList = [word]
	if word in mydict.keys():
		sinList.extend(mydict[word]['sinonim'])
		return sinList
	else:
		return sinList

# ==================================================
# Mencari antonim suatu kata
# ==================================================
def getAntonim(word):
	if word in mydict.keys():
		if 'antonim' in mydict[word].keys():
			return mydict[word]['antonim']

	return []