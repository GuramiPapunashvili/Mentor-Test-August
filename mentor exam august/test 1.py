def ten_minute_walk(arr):
    starting_point = {
        'n':'s',
        's':'n',
        'e':'w',
        'w':'e'
    }
    if len(arr) == 10:
        if arr.count('n') == arr.count('s') and arr.count('e') == arr.count('w'):
            return True
    return False
print(ten_minute_walk(['e', 'w', 'e', 'w', 'n', 's', 'n', 's', 'e', 'w']))    