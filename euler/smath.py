# I am using this as my own library for the things that I want to implement, 
# but also is resused alot throught out Project Euler.

import math

def isPrime(n: int) -> bool:
    '''
    Checks if number is prime
    ### Arguments
    **n**: positive integer
    ### Return
    returns True if n is prime
    '''
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


def factorization(n : int, prime=True, recur=True) -> list:
    '''
    Factor an integer
    ### Arguments
    **n**: positive integer<br>
    **prime**(opt): get prime factorization | Default: True<br>
    **recur**(opt): use recursive algorithm | Default: True<br>

    ### Return
    list of factors
    '''
    if recur and prime:
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
        return factorization(a) + factorization(b)
    
