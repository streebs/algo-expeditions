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

def isPal(n):
    n = str(n)

    a = ""
    b = ""
    length = len(n)

    if length % 2 == 0:
        mid = int(length/2)
        a = n[:mid]
        b = n[mid:]
    else:
        mid = int(length/2)
        a = n[:mid]
        b = n[mid+1:]

    if a == b[::-1]:
        return True
    else:
        return False

def findPal():
    UPPER = 998002
    LOWER = 100
    pals = []
    for i in range(LOWER, UPPER):
        pals.append(i) if isPal(i) else ...

    return pals

def factorPal():

    for pal in reversed(findPal()):
        if isPrime(pal):
            continue

        a = 0
        b = 0

        for i in range(100, pal):
            if pal % i == 0:
                a = i
                b = int(pal / a)

                if a >= 100 and a <= 999 and b >= 100 and b <= 999:
                    return pal
                
t1 = time.time()
factorPal()
t2 = time.time()
print(f"exercise took: {t2-t1}")
