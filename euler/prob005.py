# a number that I can think of that is divisible by all the numbers from 1-20 would be 20!
# is there anything I can glean from that fact?

# Brute Force Approach: test every number less that 20! (which is insanley huge)

# sieve approach: can I do something similar to the sieve of erastothenes with primes?

# categorise factors and combine: anything divisible by 18 is also divisible by  2, 3, and 6.

# 20: 10, 5, 4, 2
# 19: 19
# 18: 6, 3, 2
# 17: 17
# 16: 8, 4, 2
# 15: 5, 3
# ...

# make 20 sets of all the factors for each number from 1-20 (This approach did not work)

#                                 *** ANSWER ***
# I found the answer to this!
# The answer lies in the prime factorization!
# I dont have a super mathematical answer but I found a pattern!
# from the problem we know that the smallest multiple that is divisible by all number 1-10
# here is a list of the prime factors for each number
# 2
# 3
# 2 2
# 5
# 2 3
# 7
# 2 2 2
# 3 3
# 2 5

# if we take each column and remove repeats (one 2 not five 2's from column one)
# then the remaining numbers from each column with the repeats removed will be factors of the answer
# multiply to get the answer

import smath
from functools import reduce
from operator import mul

def check_index(lst, index):
    try:
        lst[index]
        return True
    except IndexError:
        return False

def smallest_multiple(n: int):
    factors = []
    for i in range(2, n+1):
        factorization = smath.factorization(i)
        for j in factorization:
            cnt = factors.count(j)
            fact_cnt = factorization.count(j)
            if fact_cnt > cnt:
                factors.append(j)

    return reduce(mul, factors)



print(smallest_multiple(20))



