from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import re
from tesaurus import *
from BM import *
from kmp import *
from regex import *

stopword = StopWordRemoverFactory().create_stop_word_remover()

pertanyaan = []
jawaban = []
for line in open('pertanyaan.txt').readlines():
    i = 0
    j = 0
    while (line[j] != ' '):
        j+=1
    while (line[i] != '?'):
        i+=1   
    pertanyaan.append(stopword.remove((line[j+1:i+2].lower())))
    jawaban.append(line[i+2:len(line)-1])

while(True):
    query = input("Masukkan Query : ").lower()
    print()
    query = stopword.remove(query)
    querylist = query.split(' ')
    synonymList = []
    for queryWord in querylist:
        synonymList.append(getSinonim(queryWord))
    #dikombinasi
    sentenceList = [[]]
    for word in synonymList:
        newList = []
        for synonym in word:
            for sentence in sentenceList:
                newList.append(sentence+[synonym])
        sentenceList = newList

    pertanyaanRekomendasi = []
    #maxi = 0

    for sentence in sentenceList:
        sentence = (' '.join(sentence))
        regexQuery = regex(sentence)
        i = 0
        for p in pertanyaan:
            found = False
            rgx = re.search(regexQuery, p)
            kmp = find_occurrences(p, sentence)/len(p)
            bm = bmMatch(p, sentence)/len(p)
            #kecocokan diatas 90%
            #maxi = max(maxi,max(kmp,bm))
            if(kmp>=0.9 or bm >= 0.9 or rgx):
                found = True
                break
            elif(kmp>=0.6 or bm >= 0.6 and len(pertanyaanRekomendasi)<3):
                pertanyaanRekomendasi.append(p)
            #kalo gaada 90%, sementara diadd dulu ke pertanyaan yang diatas 60%
            i+=1
        if found:
            break
        #diproses, cari secara KMP, Boyer-Moore, dan Regex
        #kalo ketemu, break
        #kalo ga ketemu, cari 60% keatas, kasih rekomendasi pertanyaan
        #kalo ga ketemu samsek, alihin pembicaraan
    #print(str(maxi))
    if found:
        print(jawaban[i])
    elif(len(pertanyaanRekomendasi)!=0):
        print("Apakah maksud anda : ")
        for x in pertanyaanRekomendasi:
            print(x)
    else:
        print("Aku tidak mengerti maksud pertanyaanmu. ")
        print("Ngomong-ngomong, tahukah kamu bahwa kita bernafas kira-kira 23.000 kali setiap harinya!")
        print("Ya kalau aku engga sih hehe")
        #fakta gaje lah wkwk
        print()
        print("Silahkan coba tanya aku lagi untuk fakta lainnya!")
    print()