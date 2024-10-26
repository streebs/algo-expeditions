# a * b = c

# 1,2,3,4,6,12
# 1,3,5,15
# 1,2,4
# 1,3,9
# 1,2,4,8,16

import math
import time

def isPrime(n):
    # find the sqrt of n and round up
    if n == 2:
        return True
    if n == 1:
        return False
    
    x = math.floor(n**.5)
    for i in range(2, x+1):
        if n % i == 0:
            return False

    return True 


def largestPrimeFactor(n):
    # if n is prime return n
    if isPrime(n):
        return [n]
    # find 2 facors of n and recurse
    a = 0
    b = 0
    for i in range(2, n):
        if n % i == 0:
            a = i
            b = int(n / a)
            break
    return largestPrimeFactor(a) + largestPrimeFactor(b)

NUM = 600851475143

t1 = time.time()
largestPrimeFactor(NUM)
t2 = time.time()

print(f"exercise took: {t2-t1}")
# print(isPrime(100000001))