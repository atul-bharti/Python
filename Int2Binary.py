def to_binary(num):

    binary = ''
    while num >= 2:
        binary =  str(num % 2) + binary
        num = num // 2

    return str(num) + binary


print(to_binary(233))