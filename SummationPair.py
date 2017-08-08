def pair(numlist,sum):
    numDict = {}
    for i in numlist:
        if not numDict.__contains__(i):
            numDict[i] = 1
        if numDict.__contains__(sum - i):
            print('Pain',i,sum-i)


pair([1,2,3,5,8,9,4],5)