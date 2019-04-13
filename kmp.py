def find_occurrences(S,p):
    """
    Jika ditemukan, return index lokasi ditemukan.
    Jika tidak, return []
    """
    matches = []
    f = prefix(p)
    n, m = len(S), len(p)
    j = 0
    for i in range(n):
      while j >= 0 and S[i] != p[j]:
         if j > 0: j = f[j-1]
         else: j = -1
      j += 1  
      if j == m:
         j = f[m-1]
         matches.append(i-m+1)
    return matches

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

