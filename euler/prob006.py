import smath


def sum_square_difference(limit: int):
    sum_of_squares = 0
    sum = 0
    for i in range(1, limit+1):
        sum += i
        sum_of_squares += i*i

    square_of_sum = sum * sum

    return square_of_sum - sum_of_squares

print(sum_square_difference(100))