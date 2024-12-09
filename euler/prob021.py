import smath.smath as smath

def d(n: int):
    return sum(smath.factorization(n, True))

def amicable_numbers(n: int):
    cache = []

    for i in range(2, n):
        b = d(i)
        if b == i: # anumber cannot be amicable with itself
            continue
        if d(b) == i and (b not in cache or i not in cache):
            cache.append(i)
            cache.append(b)
    
    return sum(cache)

print(amicable_numbers(10000))

# print(d(28))
