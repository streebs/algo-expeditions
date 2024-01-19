
import aocd
import unittest
import sys
from missing import *

# UPDATE DAY for 
DAY = 7

card_values = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 11,
    'Q': 12,
    'K': 13,
    'A': 14
}

class Hand:
    def __init__(self, hand : str, bid : int):
        self.hand = hand
        self.bid = bid
        self.type = self.getType()

    def getType(self):
        possible1 = [(1,1,1,1,1)]
        possible2 = [(2,1,1,1),(1,2,1,1),(1,1,2,1),(1,1,1,2)]
        possible3 = [(2,2,1),(2,1,2),(1,2,2)]
        possible4 = [(3,1,1),(1,3,1),(1,1,3)]
        possible5 = [(2,3),(3,2)]
        possible6 = [(4,1),(1,4)]
        possible7 = [(5,)]

        cards = {}
        for i in self.hand:
            if i in cards:
                cards[i] += 1
            else:
                cards[i] = 1
        
        # type 1 -- High Card
        if tuple(cards.values()) in possible1:
            return 1
        # type 2 -- One Pair
        if tuple(cards.values()) in possible2:
            return 2
        # type 3 -- Two Pair
        if tuple(cards.values()) in possible3:
            return 3
        # type 4 -- Three of a Kind
        if tuple(cards.values()) in possible4:
            return 4
        # type 5 -- Full House
        if tuple(cards.values()) in possible5:
            return 5
        # type 6 -- Four of a Kind
        if tuple(cards.values()) in possible6:
            return 6
        # type 7 -- Five of a Kind
        if tuple(cards.values()) in possible7:
            return 7
        
        raise ValueError("Missed Card Type: " + str(tuple(cards.values())))
        

    def __lt__(self, other):
        if self.type < other.type:
            return True
        elif self.type == other.type:
            for c in range(5):
                if card_values[self.hand[c]] < card_values[other.hand[c]]:
                    return True
                elif card_values[self.hand[c]] > card_values[other.hand[c]]:
                    return False
        else:
            return False

                
    def __repr__(self):
        return self.hand

class JokerHand:
    def __init__(self, hand : str, bid : int):
        self.hand = hand
        self.bid = bid
        self.type = self.getType()

    def getType(self):
        possible1 = [(1,1,1,1,1)]
        possible2 = [(2,1,1,1),(1,2,1,1),(1,1,2,1),(1,1,1,2)]
        possible3 = [(2,2,1),(2,1,2),(1,2,2)]
        possible4 = [(3,1,1),(1,3,1),(1,1,3)]
        possible5 = [(2,3),(3,2)]
        possible6 = [(4,1),(1,4)]
        possible7 = [(5,)]

        cards = {}
        for i in self.hand:
            if i in cards:
                cards[i] += 1
            else:
                cards[i] = 1
        
        # type 1 -- High Card
        if tuple(cards.values()) in possible1:
            return 1
        # type 2 -- One Pair
        if tuple(cards.values()) in possible2:
            return 2
        # type 3 -- Two Pair
        if tuple(cards.values()) in possible3:
            return 3
        # type 4 -- Three of a Kind
        if tuple(cards.values()) in possible4:
            return 4
        # type 5 -- Full House
        if tuple(cards.values()) in possible5:
            return 5
        # type 6 -- Four of a Kind
        if tuple(cards.values()) in possible6:
            return 6
        # type 7 -- Five of a Kind
        if tuple(cards.values()) in possible7:
            return 7
        
        raise ValueError("Missed Card Type: " + str(tuple(cards.values())))
        

    def __lt__(self, other):
        if self.type < other.type:
            return True
        elif self.type == other.type:
            for c in range(5):
                if card_values[self.hand[c]] < card_values[other.hand[c]]:
                    return True
                elif card_values[self.hand[c]] > card_values[other.hand[c]]:
                    return False
        else:
            return False

                
    def __repr__(self):
        return self.hand

def part_a(data):
    list_of_hands = []
    for h in data:
        list_of_hands.append(Hand(h.split(' ')[0], int(h.split(' ')[1])))

    list_of_hands.sort()
    sum = 0
    for h in range(len(list_of_hands)):
        prod = (h+1) * list_of_hands[h].bid
        sum += prod
    
    return sum

def part_b(data):
    return 0



################# UNIT TESTS #################
test_data = [
    '32T3K 765',
    'T55J5 684',
    'KK677 28',
    'KTJJT 220',
    'QQQJA 483'
]
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(part_a(test_data), 6440)
        self.assertEqual(part_b(test_data), 0)


############### DATA RETRIEVAL ###############
if test_data == None or DAY == 0:
    raise MissingFieldsError("You have not updated either `DAY`, `test_data`, or both!")
data = aocd.get_data(day=DAY, year=2023)
data_as_list = data.split("\n")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        sys.argv = [sys.argv[0]] # unittest uses the system args to run so it has to be cleared :/
        unittest.main()
    else:
        aocd.submit(part_a(data_as_list), part='a', day=DAY, year=2023)
        # aocd.submit(part_b(data_as_list), part='b', day=DAY, year=2023)

if __name__ == "__main__":
    main()






















# class A:
#     def __init__(self, num) -> None:
#         self.num = num

#     def __lt__(self, other):
#         if self.num < other.num:
#             return True
#         else:
#             return False
#     def __le__(self, other):
#         if self.num <= other.num:
#             return True
#         else:
#             return False
        
#     def __repr__(self):
#         return str(self.num)


# l = [A(3), A(1), A(2)]

# l.sort()
# print(l)


