def find_gap(g,m,n):
    status = False
    new_number = m
    two_primes = []
    while status == False:
        if len(two_primes) < 2:
            for i in range(new_number,n):
                new_number += 1
                for x in range(2,i):
                    if i % x != 0:
                        two_primes.append(i)
        elif two_primes[0] - two_primes[-1] == g:
            return two_primes
        else:
            two_primes.clear()

    return None

print(find_gap(g = 6, m = 585348, n = 685348))                    

