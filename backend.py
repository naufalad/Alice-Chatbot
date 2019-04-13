from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import re
from tesaurus import *


db = pymysql.connect("localhost","testuser","test123","TESTDB" )
stopword = StopWordRemoverFactory().create_stop_word_remover()

query = input("Masukkan Query : ")
query = stopword.remove(query.lower())
#print(query)
querylist = query.split(' ')
synonymList = []
for queryWord in querylist:
    synonymList.append(getSinonim(queryWord))
#print(synonymList)
#dikombinasi
sentenceList = [[]]
for word in synonymList:
    newList = []
    for synonym in word:
        for sentence in sentenceList:
            newList.append(sentence+[synonym])
    sentenceList = newList

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# Create table as per requirement
sql = """CREATE TABLE EMPLOYEE (
   PERTANYAAN  CHAR(20) NOT NULL,
   JAWABAN  CHAR(20))"""

cursor.execute(sql)
cursor.execute(sql)
# disconnect from server
db.close()

for sentence in sentenceList:
    #diproses, cari secara KMP, Boyer-Moore, dan Regex
    #kalo ketemu, break
    #kalo ga ketemu, cari 60% keatas, kasih rekomendasi pertanyaan
    #kalo ga ketemu samsek, alihin pembicaraan
    print(' '.join(sentence))