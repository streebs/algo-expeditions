#########################################################################
## So this solutin is reeeeeeeaaaaaaaalllllllllyyyyyyyyy SLOW!         ##
## but, i really had fun implementing a state machine to make it work! ##
#########################################################################





import unittest
from abc import ABC, abstractmethod
import re

class AtoiMachine:

    def __init__(self):
        self.state0 = State0(self)
        self.state1 = State1(self)
        self.state2 = State2(self)
        self.state3 = State3(self)
        self.currentState = self.state0
        self.number = ''

    def getState(self):
        return self.currentState
    
    def setState(self, atoi):
        self.currentState = atoi

    def eat(self, c : str):
        self.currentState.eat(c)


class AtoiState(ABC):
    def __init__(self, atoi : AtoiMachine):
        self.atoi = atoi

    @abstractmethod
    def eat(c : str):
        pass

class State0(AtoiState):
    def __init__(self, atoi : AtoiMachine):
        super().__init__(atoi)

    def eat(self, c : str):
        if re.match(r'\+|-', c):
            self.atoi.number += c
            self.atoi.setState(self.atoi.state3)
        elif re.match(r'[ ]', c):
            self.atoi.setState(self.atoi.state0)
        elif re.match(r'[0-9]', c):
            self.atoi.number += c
            self.atoi.setState(self.atoi.state1)
        elif re.match(r'[^0-9]', c):
            self.atoi.setState(self.atoi.state2)

class State1(AtoiState):
    def __init__(self, atoi : AtoiMachine):
        super().__init__(atoi)

    def eat(self, c : str):
        if re.match(r'[0-9]', c):
            self.atoi.number += c
            self.atoi.setState(self.atoi.state1)
        elif re.match(r'[^0-9]', c):
            self.atoi.setState(self.atoi.state2)

class State2(AtoiState):
    def __init__(self, atoi : AtoiMachine):
        super().__init__(atoi)

    def eat(self, c : str):
        if self.atoi.number == '+' or self.atoi.number == '-' or self.atoi.number == '':
            self.atoi.number = '0'

class State3(AtoiState):
    def __init__(self, atoi : AtoiMachine):
        super().__init__(atoi)

    def eat(self, c : str):
        if re.match(r'[0-9]', c):
            self.atoi.number += c
            self.atoi.setState(self.atoi.state1)
        elif re.match(r'[^0-9]', c):
            self.atoi.setState(self.atoi.state2)


def myAtoi(s):
    s = s + 'epsilon'
    atoi = AtoiMachine()

    for c in s:
        atoi.eat(c)

    x = int(atoi.number)
    return x if x <= 2**31 - 1 and x >= (-2)**31 else 2**31 - 1 if x > 2**31 - 1 else (-2)**31 if x < (-2)**31 else ...

    
        
        

    



# def myAtoi(s):
#     # x = int(s)
#     # return x if x <= 2**31 - 1 and x >= (-2)**31 else 2**31 - 1 if x > 2**31 - 1 else (-2)**31 if x < (-2)**31 else ...

#     # numStr = ''
#     # for c in s:
#     #     numStr = numStr + c if (ord(c) >= 48 and ord(c) <= 57) or (c == '-') else numStr
#     # x = int(numStr) if numStr != '' else 0
#     # return x if x <= 2**31 - 1 and x >= (-2)**31 else 2**31 - 1 if x > 2**31 - 1 else (-2)**31 if x < (-2)**31 else ...
    
#     acceptLeads = ['0','1','2','3','4','5','6','7','8','9','+','-',' ']
#     numStr = ''
#     for c in s:
#         if c in acceptLeads:
#             numStr = numStr + c
#         if c not in acceptLeads and numStr == '':
#             numStr = '0'
#             break
#         if c not in acceptLeads:
#             break

#         # open = False if c not in acceptLeads else True
#         # numStr = numStr + c if c in acceptLeads and open == True else ...
#     x = int(numStr)
#     return x if x <= 2**31 - 1 and x >= (-2)**31 else 2**31 - 1 if x > 2**31 - 1 else (-2)**31 if x < (-2)**31 else ...


class TestMyAtoi(unittest.TestCase):
    def test_myAtoi(self):
        self.assertEqual(myAtoi("42"), 42)
        self.assertEqual(myAtoi("   -42"), -42)
        self.assertEqual(myAtoi("4193 with words"), 4193)
        self.assertEqual(myAtoi("words with 987"), 0)
        self.assertEqual(myAtoi("+-12"), 0)
        self.assertEqual(myAtoi("+"), 0)
        self.assertEqual(myAtoi("-17653"), -17653)
        self.assertEqual(myAtoi("12341234123412341234"), 2**31-1)
        self.assertEqual(myAtoi("-12341234123412341234"), (-2)**31)

if __name__ == '__main__':
    unittest.main()
