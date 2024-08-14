def remove_similar(arr, arr2):
    arr2_elements = [i for i in arr2]
    res = []
    for i in arr:
        if i not in arr2_elements:
            res.append(i)
        else:
            continue
    return res

print(remove_similar([-8, -2, -4, 13, 10, -12, -3, 6],[-3, 17]))            