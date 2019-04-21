from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
import re, string
from tesaurus import *
import sys




#ALGORITMA KMP
def find_occurrences(S,p):

    matches = -1
    count = 0
    maxcount = 0
    f = prefix(p)
    n, m = len(S), len(p)
    j = 0
    for i in range(n):
      if S[i] == p[j]:
         count+=1
      while j >= 0 and S[i] != p[j]:
         if(count>maxcount):
            maxcount = count
         count = 0
         if j > 0: j = f[j-1]
         else: j = -1
      j += 1  
      if j == m:
         j = f[m-1]
         matches = (i-m+1)
         break
    
    if(count>maxcount):
      maxcount = count
    return maxcount

def prefix(p):
    m = len(p)
    pi = [0]*m
    j = 0 
    for i in range(1,m):
      while j >= 0 and p[j] != p[i]:
         if j-1 >= 0:
                j = pi[j-1]
         else:
                j = -1 
      j += 1
      pi[i] = j
    return pi

#ALGORITMA BM
def bmMatch(text, pattern):
    last = buildLast(pattern)
    n = len(text)
    m = len(pattern)
    i = m-1
    count = 0
    maxcount = 0

    if(i>n-1):
        return count
    j = m-1
    while(i<n and j<m):
        if(pattern[j] == text[i]):
            count+=1
            if(j==0):
                maxcount = count
                break
            else:
                i-=1
                j-=1
        else:
            if(count>maxcount):
                maxcount = count
            count = 0
            lo = last[ord(text[i])]
            i += m - min(j,1+lo)
            j = m-1
        if(1 > n-1):
            break
    return maxcount


def buildLast(pattern):
    last = [None] * 128
    for i in range(128):
        last[i] = -1
    for i in range(len(pattern)):
        last[ord(pattern[i])] = i
    return last
#ALGORITMA REGEX, buat nambahin sebuah pattern jadi ada query regexnya
def regex(S):
    S = S.replace('kah', '(kah)?')
    if(S.find('mengapa') != -1):
        S = S.replace('mengapa', 'mengapa|kenapa')
    else:
        S = S.replace('kenapa', 'mengapa|kenapa')
    if(S.find('bagaimana') != -1):
        S = S.replace('bagaimana', 'bagaimana|gimana')
    else:
        S.replace('gimana', 'gimana|bagaimana')
        
    S = S.replace(' ', '.*')
    return S

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
    pertanyaan.append(stopword.remove((line[j+1:i].lower())))
    jawaban.append(line[i+2:len(line)-1])

query = re.sub('[%s]' % re.escape(string.punctuation), '', sys.argv[1].lower())
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
#print(maxi)
if found:
    output = jawaban[i]
elif(len(pertanyaanRekomendasi)!=0):
    output = "Apakah maksud anda : "
    for x in pertanyaanRekomendasi:
        output+= '\n' + x
else:
    output = "Aku tidak mengerti maksud pertanyaanmu.\nNgomong-ngomong, tahukah kamu bahwa kita bernafas kira-kira 23.000 kali setiap harinya!\nYa kalau aku engga sih hehe\n\nSilahkan coba tanya aku lagi untuk fakta lainnya!"
    #fakta gaje lah wkwk
print(output)
print()