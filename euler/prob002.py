import time

# Find the nth term of the fib sequence
def fib(n):
    if n <= 1:
        return 1
    if n <= 2:
        return 2
    return fib(n-1) + fib(n-2)

def fibIter(n):
    
    first = 1
    second = 2
    i = 1
    while i < n:
        next = first + second
        first = second
        second = next
        i += 1
    return first

def fibEvenSumIter():
    i = 1
    sum = 0
    while i > 0:
        x = fibIter(i)
        if x >= 4000000:
            break
        if x % 2 == 0:
            sum += x
        i += 1

    return sum

def fibEvenSumRec():
    i = 1
    sum = 0
    while i > 0:
        x = fib(i)
        if x >= 4000000:
            break
        if x % 2 == 0:
            sum += x
        i += 1

    return sum


t1 = time.time()

fibEvenSumIter()

t2 = time.time()

t3 = time.time()

fibEvenSumRec()

t4 = time.time()

iterTime = t2-t1
recTime = t4-t3

print(f"Iteration: {iterTime}")
print(f"Recusion: {recTime}")
print(f"Iteration is {(recTime - iterTime) / (recTime) * 100}% faster!")
