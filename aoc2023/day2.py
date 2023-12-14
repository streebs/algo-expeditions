import aocd
import unittest
import sys
import requests

import re

def validate(r, g, b):
    if r <= 12 and g <= 13 and b <= 14:
        return True
    else:
        return False

def part_a(data_as_list):
    
    validGames = []
    for line in data_as_list:
        a = line.split(':') # a = ['Game 1', '3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green']
        gameNum = int(a[0].split(' ')[-1])

        validPlays = []
        plays = a[1].split(';') # plays = ['3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green']
        for play in plays:
            diceResults = play.split(',') # diceResults = ['3 blue','4 red']

            validResults = []
            for result in diceResults:
                r = 0
                g = 0
                b = 0
                result = result.lstrip(' ')
                if re.match(r'\d+ red', result):
                    r = int(result.split(' ')[0])
                if re.match(r'\d+ green', result):
                    g = int(result.split(' ')[0])
                if re.match(r'\d+ blue', result):
                    b = int(result.split(' ')[0])
                validResults.append(validate(r,g,b))
            
            if False not in validResults:
                validPlays.append(True)
            else:
                validPlays.append(False)
        if False not in validPlays:
            validGames.append(gameNum)

    return sum(validGames)





def part_b(data_as_list):

    powers = []
    for line in data_as_list:
        games = line.split(':')[1]

        reds = []
        greens = []
        blues = []

        redsText = re.findall(r'\d+ red', games)
        greensText = re.findall(r'\d+ green', games)
        bluesText = re.findall(r'\d+ blue', games)

        for r in redsText:
            reds.append(int(r.split(' ')[0]))
        for g in greensText:
            greens.append(int(g.split(' ')[0]))
        for b in bluesText:
            blues.append(int(b.split(' ')[0]))

        maxRed = max(reds)
        maxGreen = max(greens)
        maxBlues = max(blues)

        powers.append(maxRed * maxGreen * maxBlues)

    return sum(powers)
        


################# UNIT TESTS #################
test_data = game_data = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]

class TestPartA(unittest.TestCase):
    def test_part_a(self):
        self.assertEqual(part_a(test_data), 8)

class TestPartB(unittest.TestCase):
    def test_part_b(self):
        self.assertEqual(part_b(test_data), 2286)


############### DATA RETRIEVAL ###############
# data = aocd.get_data(day=1, year=2023)
# data_as_list = data.split("\n")
        
url = 'https://adventofcode.com/2023/day/2/input'
cookies = {'session':'53616c7465645f5f02f46aae4bb05cb8ab6d077207b58a91998d6b6103e0b82405ecf051b5a249be678a6f0241a87c686ecd8bff6c0d6c92df8bb6d046eea358'}
r = requests.get(url, cookies=cookies)
data = r.text
data_as_list = data.split("\n")
data_as_list = data_as_list[:-1]



def main():
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        sys.argv = [sys.argv[0]] # unittest uses the system args to run so it has to be cleared :/
        unittest.main()
    else:
        print("Part A: " + str(part_a(data_as_list)))
        print("Part B: " + str(part_b(data_as_list)))
    #     aocd.submit(part_a(data_as_list), part='a', day=1, year=2023)
    #     aocd.submit(part_b(data_as_list), part='b', day=1, year=2023)

if __name__ == "__main__":
    main()