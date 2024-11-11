


import smath

def nth_prime(n: int):
    cnt = 1
    i = 1
    while True:
        if smath.isPrime(i):
            if cnt == n:
                return i
            i += 1
            cnt += 1
            continue
        i += 1


print(nth_prime(10001))
            