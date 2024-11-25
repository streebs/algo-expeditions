

def fact(n):
    if n == 0 or n == 1:
        return 1
    
    return n * fact(n-1)

def fact_digit_sum():
    num_str = str(fact(100))

    digits = [int(x) for x in num_str]

    return sum(digits)

print(fact_digit_sum())