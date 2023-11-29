import unittest


def myAtoi(s):
    # x = int(s)
    # return x if x <= 2**31 - 1 and x >= (-2)**31 else 2**31 - 1 if x > 2**31 - 1 else (-2)**31 if x < (-2)**31 else ...

    # numStr = ''
    # for c in s:
    #     numStr = numStr + c if (ord(c) >= 48 and ord(c) <= 57) or (c == '-') else numStr
    # x = int(numStr) if numStr != '' else 0
    # return x if x <= 2**31 - 1 and x >= (-2)**31 else 2**31 - 1 if x > 2**31 - 1 else (-2)**31 if x < (-2)**31 else ...
    
    acceptLeads = ['0','1','2','3','4','5','6','7','8','9','+','-',' ']
    numStr = ''
    for c in s:
        if c in acceptLeads:
            numStr = numStr + c
        if c not in acceptLeads and numStr == '':
            numStr = '0'
            break
        if c not in acceptLeads:
            break

        # open = False if c not in acceptLeads else True
        # numStr = numStr + c if c in acceptLeads and open == True else ...
    x = int(numStr)
    return x if x <= 2**31 - 1 and x >= (-2)**31 else 2**31 - 1 if x > 2**31 - 1 else (-2)**31 if x < (-2)**31 else ...


class TestMyAtoi(unittest.TestCase):
    def test_myAtoi(self):
        self.assertEqual(myAtoi("42"), 42)
        self.assertEqual(myAtoi("   -42"), -42)
        self.assertEqual(myAtoi("4193 with words"), 4193)
        self.assertEqual(myAtoi("words with 987"), 0)
        self.assertEqual(myAtoi("-17653"), -17653)
        self.assertEqual(myAtoi("12341234123412341234"), 2**31-1)
        self.assertEqual(myAtoi("-12341234123412341234"), (-2)**31)

if __name__ == '__main__':
    unittest.main()
