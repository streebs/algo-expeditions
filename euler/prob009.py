# this is an interesting one. How can I find a pythagorean triple that also sums to 1000
#  without doing time consuming calculations?
# start by solving the system of equations and get a solution dependant on a (or x)

# x^2 + y^2 - z^2 = 0
# x + y + z = 1000

#solution:
# x != 1000 (in this case 0 <= x <= 999)
# y = 1000(x-500) / x - 1000
# z = -x^2 + 1000x - 500000 / x - 1000

# search for all solutions with x in its defined range

def triplet():
    for x in range(1, 1000):
        y = (1000 * (x - 500)) / (x - 1000)
        z = (x**2 * -1 + 1000 * x - 500000) / (x - 1000)
        
        if (x + y + z) == 1000 and x > 0 and y > 0 and z > 0 and y.is_integer() and z.is_integer():
            return x * y * z

print(triplet())