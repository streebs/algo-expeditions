import aocd
import unittest
import sys
import math

# UPDATE DAY for 
DAY = 5

def dataToDict(data):
    organizedData = {'seeds':[],'seed-to-soil map':[],'soil-to-fertilizer map':[],'fertilizer-to-water map':[],'water-to-light map':[],'light-to-temperature map':[],'temperature-to-humidity map':[],'humidity-to-location map':[]}
    for line in data:
        if 'seeds' in line:
            organizedData['seeds'] = [int(num) for num in line.split(':')[1].strip().split(' ')] # disgusting, I know
        elif line.split(':')[0] in organizedData:
            curMarker = line.split(':')[0]
        elif line == '':
            pass # skip empty lines
        else:
            tup = tuple([int(el) for el in line.split(' ')])
            organizedData[curMarker].append(tup)
    return organizedData

class Map:
    def __init__(self, spec : list):
        self.spec = spec

    def __getitem__(self, key):
        for s in self.spec:
            src = s[1]
            dest = s[0]
            rng = s[2]

            if key >= src and key < src + rng:
                diff = key - src
                return dest + diff
        
        return key




def part_a(data):
    formattedData = dataToDict(data)
    seed2soil = Map(formattedData['seed-to-soil map'])
    soil2fert = Map(formattedData['soil-to-fertilizer map'])
    fert2water = Map(formattedData['fertilizer-to-water map'])
    water2light = Map(formattedData['water-to-light map'])
    light2temp = Map(formattedData['light-to-temperature map'])
    temp2humid = Map(formattedData['temperature-to-humidity map'])
    humid2location = Map(formattedData['humidity-to-location map'])

    locations = []
    for s in formattedData['seeds']:
        locations.append(humid2location[temp2humid[light2temp[water2light[fert2water[soil2fert[seed2soil[s]]]]]]])
    
    return min(locations)


def part_b(data):
    formattedData = dataToDict(data)
    seed = formattedData['seeds']
    formattedSeeds = [(seed[i], seed[(i+1)%len(seed)]) for i in range(0,len(seed),2)]

    seed2soil = Map(formattedData['seed-to-soil map'])
    soil2fert = Map(formattedData['soil-to-fertilizer map'])
    fert2water = Map(formattedData['fertilizer-to-water map'])
    water2light = Map(formattedData['water-to-light map'])
    light2temp = Map(formattedData['light-to-temperature map'])
    temp2humid = Map(formattedData['temperature-to-humidity map'])
    humid2location = Map(formattedData['humidity-to-location map'])

    smallestNum = math.inf
    for f in formattedSeeds:
        start = f[0]
        end = f[1]
        for i in range(start, start+end):
             t = humid2location[temp2humid[light2temp[water2light[fert2water[soil2fert[seed2soil[i]]]]]]]
             if t < smallestNum:
                 smallestNum = t
    
    return smallestNum



################# UNIT TESTS #################

def testMappage(data, key, input):
    formattedData = dataToDict(data)
    a = Map(formattedData[key])
    return a[input]

test_data = [
    'seeds: 79 14 55 13',
    '',
    'seed-to-soil map:',
    '50 98 2',
    '52 50 48',
    '',
    'soil-to-fertilizer map:',
    '0 15 37',
    '37 52 2',
    '39 0 15',
    '',
    'fertilizer-to-water map:',
    '49 53 8',
    '0 11 42',
    '42 0 7',
    '57 7 4',
    '',
    'water-to-light map:',
    '88 18 7',
    '18 25 70',
    '',
    'light-to-temperature map:',
    '45 77 23',
    '81 45 19',
    '68 64 13',
    '',
    'temperature-to-humidity map:',
    '0 69 1',
    '1 0 69',
    '',
    'humidity-to-location map:',
    '60 56 37',
    '56 93 4'
]
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(testMappage(test_data,'seed-to-soil map', 79), 81)
        self.assertEqual(testMappage(test_data,'seed-to-soil map', 14), 14)
        self.assertEqual(testMappage(test_data,'seed-to-soil map', 55), 57)
        self.assertEqual(testMappage(test_data,'seed-to-soil map', 13), 13)

        self.assertEqual(part_a(test_data), 35)
        self.assertEqual(part_b(test_data), 46)


############### DATA RETRIEVAL ###############
data = aocd.get_data(day=DAY, year=2023)
data_as_list = data.split("\n")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        sys.argv = [sys.argv[0]] # unittest uses the system args to run so it has to be cleared :/
        unittest.main()
    else:
        aocd.submit(part_a(data_as_list), part='a', day=DAY, year=2023)
        aocd.submit(part_b(data_as_list), part='b', day=DAY, year=2023)

if __name__ == "__main__":
    main()