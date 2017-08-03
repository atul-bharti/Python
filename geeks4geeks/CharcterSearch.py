def char_search(str,pat):
    char_dict = {}
    for i in range(len(str)):
        if not char_dict.__contains__(str[i]):
            char_dict[str[i]] = i

    min = len(str) + 1
    for i in pat:
        if char_dict.__contains__(i):
            pos = char_dict[i]
            if pos < min:
                min = pos

    if min > len(str):
        print('No Character found')
    else:
        print(str[min])



char_search('adcffaet','onkl')