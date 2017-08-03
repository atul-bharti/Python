def print_palindrome_string(input):
    if not input:
        return
    if(len(input) == 1):
        print(input)
        return
    else:
        if is_palindrome(input):
            print(input)
        for i in range(len(input)):
            for j in range(1,len(input) +1  ):
                if i != j:
                    newStr = input[i :j]
                    if is_palindrome(newStr):
                       print(newStr)




def is_palindrome(str):
    return str == str[::-1]


print_palindrome_string('abaaa')