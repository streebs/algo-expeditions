# Problem 1
# Find the sum of all multiples of {a,b | a,b < 1000}

# 3x < n
# x < n / 3

# a^n % b for all n

# multiples of 2, 4 less than 15
# [2,4,6,8,10,12,14]
# sum of that is 

import math

def findMultiples(a, b, n):
    amul = []
    for x in range(0, n // a + 1):
        if a * x < n:
            amul.append(a*x)
    bmul = []
    for x in range(0, n // b + 1):
        if b * x < n:
            bmul.append(b*x)

    # aMultiples = [a * x for x in range(0, (round(n/a)))]
    # bMultiples = [b * x for x in range(0, (round(n/b)))]
    multiples = amul + bmul

    multiples = set(multiples)

    sum = 0
    for mul in multiples:
        sum += mul
    
    return sum


print(findMultiples(3,5,1000))