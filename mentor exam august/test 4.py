def outliner(arr):
    count = 0
    for i in arr:
        if i % 2 == 0:
            count += 1
    if count > 1:
        for i in arr:
            if i % 2 == 1:
                return i
    else:
        for i in arr:
            if i % 2 == 0:
                return i        
            

print(outliner([-4207752, 362590, 5205484, 11340, 3740336, 1360605]))                        