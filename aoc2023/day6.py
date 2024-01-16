import aocd
import unittest
import sys

# UPDATE DAY for 
DAY = 6

def calculateDist(t, maxTime):
    return -(t**2) + t*maxTime


def part_a(data):
    times = data[0]
    distances = data[1]
    
    times = times.split(':')[1].split()
    distances = distances.split(':')[1].split()

    combinedData = {int(times[i]) : int(distances[i]) for i in range(len(times))}

    winsProd = 1
    for holdTime, RecordDist in combinedData.items():
        winsSum = 0
        for i in range(0, holdTime + 1):
            if calculateDist(i, holdTime) > RecordDist:
                winsSum += 1
        winsProd *= winsSum
        

    return winsProd


def part_b(data):
    times = data[0]
    distances = data[1]

    times = times.split(':')[1].split()
    time = ''
    for t in times:
        time += t
    
    distances = distances.split(':')[1].split()
    dist = ''
    for d in distances:
        dist += d

    time = int(time)
    dist = int(dist)

    winsSum = 0
    for i in range(time):
        if calculateDist(i, time) > dist:
                winsSum += 1
    
    return winsSum



################# UNIT TESTS #################
test_data = [
    'Time:      7  15   30',
    'Distance:  9  40  200'
]
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(part_a(test_data), 288)
        self.assertEqual(part_b(test_data), 71503)


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