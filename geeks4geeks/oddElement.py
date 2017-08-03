def mysearch(arr):
    a = (len(arr) - 1 )
    mid = a//2
    if arr[mid] != arr[mid -1 ] and arr[mid] != arr[mid + 1]:
        return arr[mid]
    if arr[mid] == arr[mid-1]:
        #element is in right side
        if mid == 1:
            return arr[mid+1]
        mysearch(arr[mid+1:])
    else:
        #elemnt is in left side
        if mid == 1:
            return arr[mid-1]
        mysearch(arr[:mid ])

    return None
print(mysearch([1,1,3,5,5]))


# A Binary search based function to find
# the element that appears only once
def search(arr, low, high):
    # Base cases
    if low > high:
        return None

    if low == high:
        return arr[low]

    # Find the middle point
    mid = low + (high - low) // 2

    # If mid is even and element next to mid is
    # same as mid, then output element lies on
    # right side, else on left side
    if mid % 2 == 0:

        if arr[mid] == arr[mid + 1]:
            return search(arr, mid + 2, high)
        else:
            return search(arr, low, mid)

    else:
        # if mid is odd
        if arr[mid] == arr[mid - 1]:
            return search(arr, mid + 1, high)
        else:
            return search(arr, low, mid - 1)


print(search([1,1,5,5,7,9],0,5))