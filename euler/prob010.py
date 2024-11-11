import smath


def sum_of_primes(limit: int):
    i = 1
    sum = 0
    while True:
        if smath.isPrime(i):
            sum += i
        i +=1

        if i >= limit:
            break

    return sum

print(sum_of_primes(10))