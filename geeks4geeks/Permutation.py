def str_permute(str,a):
    length = len(str)
    if a == length - 1:
        print(str)
    for i in range(a,length):
        newstr = swap(str, a, i)
        str_permute(newstr, a + 1)



def swap(origarr,i,j):
    arr = origarr[:]
    arr[i] ,arr[j] = arr[j],arr[i]
    return arr

str_permute(['a','b','c'],0)