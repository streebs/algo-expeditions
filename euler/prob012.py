# for this one I know it will be far down the number line before we are even close to 500 factors
# I am gonna try to use extrapolation to get a good guess where that might begin to save some compute cycles
import smath
import time

# gonna use the factorization function to estimate when numbers start to have more than 500 factors
# print(len(smath.factorization(1000000000, prime=False)))
# this is not working and taking too long :(


def nth_triangular_number(n: int):
    return sum(range(n+1))

def divisible_triangular_number():
    i = 1
    while True:
        n = nth_triangular_number(i)
        l = smath.factorization(n, prime=False)
        print(f"{i} | {n} | {len(l)} factors")
        if len(l) > 500:
            return f"{i} | {n} | {len(l)} factors"
        i += 1

# print(len(smath.factorization(1000000000, False)))
# print(len(smath.factorization(nth_triangular_number(12375), False)))
t1 = time.time()
divisible_triangular_number()
t2 = time.time()
print(f"duration: {t2-t1}")
