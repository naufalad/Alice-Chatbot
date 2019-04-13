def bmMatch(text, pattern):
    last = buildLast(pattern)
    n = len(text)
    m = len(pattern)
    i = m-1

    if(i>n-1):
        return -1
    j = m-1
    while(True):
        if(pattern[j] == text[i]):
            if(j==0):
                return i
            else:
                i-=1
                j-=1
        else:
            lo = last[ord(text[i])]
            i += m - min(j,1+lo)
            j = m-1
        if(1 > n-1):
            break
    return -1


def buildLast(pattern):
    last = [None] * 128
    for i in range(128):
        last[i] = -1
    for i in range(len(pattern)):
        last[ord(pattern[i])] = i
    return last
