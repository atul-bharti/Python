def str_permute(str,a,b):
    for i in range(a,len(str)):
        for j in range(len(str)):
            newstr=swap(str,i,j)
            print(newstr)
            str_permute()


def swap(arr,i,j):
    arr[i] ,arr[j] = arr[j],arr[i]
    return arr