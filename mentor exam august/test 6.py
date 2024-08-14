def pig_latin(s): #Pig latin is cool
    res = []
    splitted = s.split(' ')
    for i in splitted:
        res.append(i[1:] + i[0] + 'ay')
    return res    

print(pig_latin("Cucullus non facit monachum"))