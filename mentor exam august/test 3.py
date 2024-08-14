def extended_string(num): #70304
    stringed_num = [i for i in str(num)]
    length = len(stringed_num)
    res = []
    index = 0
    for i in stringed_num:
        if int(i) != 0:
            index = stringed_num.index(str(i))
            res.append(stringed_num[index] + '0' * (length - (index + 1)))
    return str(' + '.join(res))            

print(extended_string(710163))      
