
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

wild_card_values = {
    'J': 1,     # notice how this is now worth only one
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 12,
    'K': 13,
    'A': 14
}

class Hand:
    def __init__(self, hand : str, bid : int, wilds=False):
        self.hand = hand
        self.bid = bid
        self.wilds = wilds
        self.type = self.getType()

    def getType(self):
        if self.wilds:
            hand = self.convertWilds(self.hand)
        else:
            hand = self.hand

        possible1 = [(1,1,1,1,1)] # High Card
        possible2 = [(2,1,1,1),(1,2,1,1),(1,1,2,1),(1,1,1,2)] # One Pair
        possible3 = [(2,2,1),(2,1,2),(1,2,2)] # Two Pair
        possible4 = [(3,1,1),(1,3,1),(1,1,3)] # Three of a Kind
        possible5 = [(2,3),(3,2)] # Full House
        possible6 = [(4,1),(1,4)] # Four of a Kind
        possible7 = [(5,)] # Five of a Kind

        cards = {}
        for i in hand:
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
    
    def convertWilds(self, hand : str):
        if 'J' not in hand or hand == 'JJJJJ':
            return hand
        
        # get number of wilds
        numWild = 0
        for c in hand:
            if c == 'J':
                numWild += 1

        # remove wilds from hand and replace them with '-'
        noWilds = hand.replace('J', '-')

        # find the most repeated card in the noWilds hand ignore '-'
        cards = {}
        for c in noWilds:
            cards[c] = cards[c] + 1 if c in cards and c != '-' else 1

        # organize the cards dictionary to a list of (values, keys). shamelessly stole this from https://stackoverflow.com/questions/268272/getting-key-with-maximum-value-in-dictionary
        inverse = [(value, key) for key, value in cards.items()]
        max = None
        for v in inverse:
            if v[1] == '-':
                continue
            if max == None:
                max = v
            if v[0] > max[0]:
                max = v
            if v[0] == max[0]:
                if wild_card_values[v[1]] > wild_card_values[max[1]]:
                    max = v

        highestMostRepeated = max[1]

        # highestMostRepeated = max(inverse)[1]

        # replace '-' with highestMostRepeated
        updatedHand = noWilds.replace('-', highestMostRepeated)

        return updatedHand


    def __lt__(self, other):
        if self.type < other.type:
            return True
        elif self.type == other.type:
            for c in range(5):
                if not self.wilds:
                    if card_values[self.hand[c]] < card_values[other.hand[c]]:
                        return True
                    elif card_values[self.hand[c]] > card_values[other.hand[c]]:
                        return False
                else:
                    if card_values[self.hand[c]] < wild_card_values[other.hand[c]]:
                        return True
                    elif card_values[self.hand[c]] > wild_card_values[other.hand[c]]:
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
    list_of_hands = []
    for h in data:
        list_of_hands.append(Hand(h.split(' ')[0], int(h.split(' ')[1]), wilds=True))

    list_of_hands.sort()
    sum = 0
    for h in range(len(list_of_hands)):
        prod = (h+1) * list_of_hands[h].bid
        sum += prod
    
    return sum



################# UNIT TESTS #################
test_data = [
    '32T3K 765',
    'T55J5 684',
    'KK677 28',
    'KTJJT 220',
    'QQQJA 483'
]
class Test(unittest.TestCase):
    def testA(self):
        self.assertEqual(part_a(test_data), 6440)
    def testB(self):
        self.assertEqual(part_b(test_data), 5905)


############### DATA RETRIEVAL ###############
if test_data == None or DAY == 0:
    raise MissingFieldsError("You have not updated either `DAY`, `test_data`, or both!")
data = aocd.get_data(day=DAY, year=2023)
data_as_list = data.split("\n")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        sys.argv = [sys.argv[0]] # unittest uses the system args to run so it has to be cleared :/
        unittest.main()
    elif len(sys.argv) > 1 and sys.argv[1] == '-ta':
        suite = unittest.TestLoader().loadTestsFromName("day" + str(DAY) + ".Test.testA")
        unittest.TextTestRunner().run(suite)
    elif len(sys.argv) > 1 and sys.argv[1] == '-tb':
        suite = unittest.TestLoader().loadTestsFromName("day" + str(DAY) + ".Test.testB")
        unittest.TextTestRunner().run(suite)
    elif len(sys.argv) > 1 and sys.argv[1] == '-s':
        aocd.submit(part_a(data_as_list), part='a', day=DAY, year=2023)
        aocd.submit(part_b(data_as_list), part='b', day=DAY, year=2023)
    elif len(sys.argv) > 1 and sys.argv[1] == '-sa':
        aocd.submit(part_a(data_as_list), part='a', day=DAY, year=2023)
    elif len(sys.argv) > 1 and sys.argv[1] == '-sb':
        aocd.submit(part_b(data_as_list), part='b', day=DAY, year=2023)
    else:
        print("Missing or incorrect arguments! Usage:")
        print("python aoc2023/day" + str(DAY) + ".py -t  -- for testing both parts a & b")
        print("python aoc2023/day" + str(DAY) + ".py -ta -- for testing only part a")
        print("python aoc2023/day" + str(DAY) + ".py -tb -- for testing only part b")
        print("python aoc2023/day" + str(DAY) + ".py -s  -- submit both parts a & b")
        print("python aoc2023/day" + str(DAY) + ".py -sa -- submit only part a")
        print("python aoc2023/day" + str(DAY) + ".py -sb -- submit only part b")




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


