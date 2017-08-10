def wildcard_matcher(str,pattern):
    found = True
    charMatch = False
    j = 0
    for i in range(len(pattern)):
        if pattern[i] == '*':
            i = i+1
            continue
        for k in range(j,len(str)):
            j = j + 1
            if str[k] == pattern[i]:
                charMatch = True
                break
            else:
                found = False
                return found


        if charMatch:
             continue



    return found

isMatch = wildcard_matcher('atul','a*l')
print(isMatch)