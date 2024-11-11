
def collatz(n: int, seq=[]):
    seq += [n]
    if n == 1:
        return seq
    if n % 2 == 0:
        return collatz(int(n / 2), seq)
    else:
        return collatz(3*n + 1, seq)

def longest_collatz_chain(limit: int):
    longest = [None, 0]
    for i in range(1, limit):
        l = len(collatz(i, []))
        if l > longest[1]:
            longest[0] = i
            longest[1] = l
        

    return longest

# print(len(collatz(999999)))
print(longest_collatz_chain(1000000))


   