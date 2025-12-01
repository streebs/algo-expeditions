# I am using this as my own library for the things that I want to implement, 
# but also is resused alot throught out Project Euler.

import math
import sys

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

def prime_factorization(n: int):
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
    return prime_factorization(a) + prime_factorization(b)


def factorization(n : int, proper=False) -> list:
    '''
    Factor an integer
    ### Arguments
    **n**: positive integer<br>
    **proper**(opt): returns proper devisors less than n | Default: False<br>

    ### Return
    list of factors
    '''
    if n == 1 and proper:
        return []
    if n == 1:
        return [1]
    # if n == 2 and proper:
    #     return [1]
    # if n == 2:
    #     return [1,2]
    
    a = 0
    b = 0
    factors = set()
    for i in range(1, math.ceil(n**.5)):
        if n % i == 0:
            a = i
            b = int(n / a)
            factors.add(a)
            factors.add(b)
    factors = sorted(list(factors))
    if proper:
        factors.pop()

    return factors

def linear_regression(x_vec: list, y_vec: list, y):
    n = len(x_vec)
    sum_x = sum(x_vec)
    sum_y = sum(y_vec)
    sum_xy = sum([a*b for a,b in zip(x_vec, y_vec)])
    sum_x_2 = sum([x*x for x in x_vec])

    a = (sum_y * sum_x_2 - sum_x * sum_xy) / (n * sum_x_2 - sum_x**2)
    b = (n * sum_xy - sum_x * sum_y) / (n * sum_x_2 - sum_x**2)

    # y = a + bx
    # (y - a) / b = x

    return (y - a) / b


def collatz(n: int, seq=[]):
    seq += [n]
    if n == 1:
        return seq
    if n % 2 == 0:
        return collatz(int(n / 2), seq)
    else:
        return collatz(3*n + 1, seq)
    








