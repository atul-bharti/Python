def is_anagram(str1,str2):
    if len(str1) != len(str2):
        return False
    else:
        count = 1
        strlen = len(str1)
        tmpstr = str1
        for s in range(strlen):
            tmpstr = tmpstr[count:]+tmpstr[0]
            if tmpstr == str2:
                return True

        return False


print(is_anagram('atul','tual'))