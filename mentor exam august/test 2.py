def arr_check(arr):
    if len(arr) == 0:
        return True
    for i in arr:
        if type(i) != int and type(i) != float:
            return False
        elif i % 1 != 0:
            return False
    return True    
        
print(arr_check(["-1"]))        