def non_repeat_char(str):
    charArr = [0] * 256
    charDict = {}
    frstChar = []
    for i in str:
        if not charDict.__contains__(i):
            frstChar.append(i)
            charDict[i] = 1
        else:
            frstChar.remove(i)

    print(frstChar[0])

non_repeat_char('abccba')
