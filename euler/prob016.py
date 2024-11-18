

def power_digit_sum(pow):
    big = 2**pow
    big_str = str(big)

    sum = 0
    for char in big_str:
        sum += int(char)

    return sum

print(power_digit_sum(1000))