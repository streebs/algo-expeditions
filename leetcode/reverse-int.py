import unittest

## this is really slow!
def reverseInt(target):
    order = 0
    digits = []
    isNeg = False
    if target < 0:
        target = target * -1
        isNeg = True

    while target // 10**order != 0:
        order += 1
    order -= 1

    x = target
    while order > -1:
        digits.append(x // 10**order)
        x = x % 10**order
        order = order - 1

    digits.reverse()

    num = 0
    for n in range(0, len(digits)):
        num += digits[n]*10**(len(digits)-n-1)

    if isNeg:
        num = num * -1

    return num if num <= 2**31 - 1 and num >= (-2)**31 else 0
    # print(num)

## this one is an attempt to get a faster result using built in functions
# this function is waaaayyyyy faster than the first function
def reverseInt2(x):
    # isNeg = False
    # if x < 0:
    #     x = x * -1
    #     isNeg = True
    s = str(x)
    l = list(s)
    l.reverse()
    if '-' in l:
        l.pop()
        l.insert(0, '-')
    s = ''.join(l)
    res = int(s)

    # res = int(s) if isNeg == False else int(s) * -1

    return res if res <= 2**31 - 1 and res >= (-2)**31 else 0
    
# print(reverseInt2(120))


class TestReverseInt(unittest.TestCase):
    def test_reverseInt(self):
        self.assertEqual(reverseInt(123), 321)
        self.assertEqual(reverseInt(-123), -321)
        self.assertEqual(reverseInt(120), 21)
        self.assertEqual(reverseInt(0), 0)
        self.assertEqual(reverseInt(2147483647), 0)  # This is expected to return 0 as the reversed integer overflows.

class TestReverseInt2(unittest.TestCase):
    def test_reverseInt2(self):
        self.assertEqual(reverseInt2(123), 321)
        self.assertEqual(reverseInt2(-123), -321)
        self.assertEqual(reverseInt2(120), 21)
        self.assertEqual(reverseInt2(0), 0)
        self.assertEqual(reverseInt2(2147483647), 0)  # This is expected to return 0 as the reversed integer overflows.

if __name__ == '__main__':
    unittest.main()
