import smath.smath as math



LIMIT = 28123
deficient = []
perfect = []
abundant = []

def classify():
    for n in range(1, LIMIT + 1):
        n_facts = math.factorization(n, proper=True)
        sum_facts = sum(n_facts)
        if sum_facts < n:
            deficient.append(n)
        if sum_facts == n:
            perfect.append(n)
        if sum_facts > n:
            abundant.append(n)

classify()

# remove the doubles
doubles = []
doubles_removed = []
for n in abundant:
    if n in doubles:
        doubles.append(n*2)
        continue
    else:
        doubles.append(n*2)
        doubles_removed.append(n)

total = []
length = len(doubles_removed)
for i in range(0, LIMIT+1):
    for j in range(0, length):
        if doubles_removed[j] >= i:
            continue
        for k in range(0, length):
            if doubles_removed[k] >= i:
                continue
            if i != doubles_removed[j] + doubles_removed[k]:
                total.append(i)

print(sum(total))