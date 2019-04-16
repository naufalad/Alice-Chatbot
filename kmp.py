def find_occurrences(S,p):
    """
    Jika ditemukan, return index lokasi ditemukan.
    Jika tidak, return []
    """
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


'''text = input("text : ")
pattern = input("pattern yang ingin dicari : ")
print(str(find_occurrences(text,pattern)))'''