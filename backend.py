from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import re
from tesaurus import *
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

for sentence in sentenceList:
    #diproses, cari secara KMP, Boyer-Moore, dan Regex
    #kalo ketemu, break
    #kalo ga ketemu, cari 60% keatas, kasih rekomendasi pertanyaan
    #kalo ga ketemu samsek, alihin pembicaraan
    print(' '.join(sentence))