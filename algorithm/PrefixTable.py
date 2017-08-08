def prefix_Table(pattern):
    lps = [-1]*len(pattern)
    lps[0] = 0
    for i in range(1,len(pattern)):
        j = lps[i -1] # lets assume we extending lps
        while(j > 0 and pattern[i] != pattern[j]):
            j = lps[j -1]
        if pattern[i] == pattern[j]:
            j = j +1
        lps[i] = j

    return lps

prefixTable = prefix_Table('ababcac')
print(prefixTable)
