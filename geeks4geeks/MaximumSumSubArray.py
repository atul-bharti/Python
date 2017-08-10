import sys

def max_sum_sub_array(arr):

    if len(arr) == 1:
        return arr[0]
    sum = 0
    max = arr[0]
    for i in arr:

        sum = sum + i
        if sum < 0:
            sum = 0
        else:
            if max < sum:
                max = sum

    return max

line = input()

for i in range(int(line)):
    arrLen=int(input())
    arr=list(map(int,input().split()))
    print(max_sum_sub_array(arr))

arr1 = [-1,-2,-3]
#print(max_sum_sub_array(arr1))
