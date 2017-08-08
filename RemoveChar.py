def remove_char(str,pat):
    charArr = [0]*256
    newStr = ''
    for i in str:
        charArr[ord(i)] = charArr[ord(i)] + 1
    for j in pat:
        charArr[ord(j)] = 0
    for k in str:
        if charArr[ord(k)] != 0:
          newStr = newStr +   k

    print(newStr)

remove_char('abcdeffgg','afc')