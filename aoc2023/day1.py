import aocd
import regex as re
import sys
import unittest



def part_a(data_as_list):

    total = 0

    for string in data_as_list:
        firstNum = ''
        lastNum = ''
        for char in string:
            if firstNum == '' and char.isdigit():
                firstNum = char
            if firstNum != '' and char.isdigit():
                lastNum = char

        num = firstNum + lastNum
        total += int(num)
    
    return total

def part_b(data_as_list):

    total = 0
    numbers = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}


    for string in data_as_list:
        nums = re.findall(r'([0-9]|zero|one|two|three|four|five|six|seven|eight|nine)', string, overlapped=True)
        # matches = re.finditer(r'(?:[0-9]|zero|one|two|three|four|five|six|seven|eight|nine)', string)
        # nums = [match.group(1) for match in matches]
        if len(nums) == 1:
            if nums[0] in numbers:
                nums[0] = numbers[nums[0]]
            total += int(str(nums[0]) + str(nums[0]))
        else:
            if nums[0] in numbers:
                nums[0] = numbers[nums[0]]
            if nums[-1] in numbers:
                nums[-1] = numbers[nums[-1]]

            firstNum = str(nums[0])
            lastNum = str(nums[-1])
            num = int(firstNum + lastNum)
            total += num

    return total

data = aocd.get_data(day=1, year=2023)
data_as_list = data.split("\n")


test_strings = ['two1nine', 'eightwothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen', 'asdfonefdsa', 'sevenine']
class testPartB(unittest.TestCase):
    def test_part_b(self):
        self.assertEqual(part_b(test_strings), 361)

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '-t':
        sys.argv = [sys.argv[0]] # unittest uses the system args to run so it has to be cleared :/
        unittest.main()
    else:
        aocd.submit(part_a(data_as_list), part='a', day=1, year=2023)
        aocd.submit(part_b(data_as_list), part='b', day=1, year=2023)

if __name__ == "__main__":
    main()



