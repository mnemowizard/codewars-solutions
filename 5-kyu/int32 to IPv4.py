# kata: https://www.codewars.com/kata/52e88b39ffb6ac53a400022e/python
def int32_to_ip(int32):
    res = ['0','.','0','.','0','.','0']
    int2 = ''
    count = 0
    while int32:
        append_num = int32 % 2
        int2 += str(append_num)
        int32 //= 2
        count += 1
        if count == 8 and int32:
            count = 0
            int2 += '.'
    else:
        try:
            int2 = int2[::-1].split('.')
            octet1 = sum([int(d)*2**i for i, d in enumerate(int2[0][::-1])])
            octet2 = sum([int(d)*2**i for i, d in enumerate(int2[1][::-1])])
            octet3 = sum([int(d)*2**i for i, d in enumerate(int2[2][::-1])])
            octet4 = sum([int(d)*2**i for i, d in enumerate(int2[3][::-1])])
        except:
            pass
    try:

        res[0] = str(octet1)
        res[2] = str(octet2)
        res[4] = str(octet3)
        res[6] = str(octet4)
    except:
        pass
    return ''.join(res)

result = int32_to_ip(32)
print(result)
