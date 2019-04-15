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

text = input("text : ")
pattern = input("pattern yang ingin dicari : ")
print(str(bmMatch(text,pattern)/len(pattern) * 100) + '%')