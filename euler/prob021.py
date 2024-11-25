import smath

def d(n: int):
    return sum(smath.factorization(n, True))

def amicable_numbers():
    d_nums_10 = []
    for i in range(10000):
        d_nums_10.append(d(i))

    return d_nums_10


print(amicable_numbers())
