digits = {
    "0": "zero",
    "1": "one",
    "2": "two", 
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine"
}
teens = {
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen"
} 
tens = {
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
}


def written_num(n : int):
    n_str = str(n)
    spelling = ""
    l = len(n_str)
    if l == 4:
        spelling += "onethousand"
    if l == 3:
        if n_str[0] == "1":
            spelling += "onehundred"
        else:
            spelling += digits[n_str[0]] + "hundred"
        if n_str[1] == "1":
            spelling += "and" + teens[n_str[1:]]
        elif n_str[1] == "0" and n_str[2] == "0":
            ...
        elif n_str[1] == "0" and n_str[2] != "0":
            spelling += "and" + digits[n_str[2]]
        else:
            if n_str[2] == "0":
                spelling += "and" + tens[n_str[1]]
            else:
                spelling += "and" + tens[n_str[1]] + digits[n_str[2]]

    if l == 2:
        if n_str[0] == "1":
            spelling += teens[n_str]
        else:
            if n_str[1] == "0":
                spelling += tens[n_str[0]]
            else:
                spelling += tens[n_str[0]] + digits[n_str[1]]
    if l == 1:
        spelling += digits[n_str]

    return spelling



def number_letter_counts():
    spelling = ""
    for i in range(1, 1001):
        s = written_num(i)
        print(s)
        spelling += s
    print()
    return len(spelling)


print(number_letter_counts())


# print(len(written_num(342)))
# print(len(written_num(115)))
# print()

# print(written_num(3))
# print(written_num(14))
# print(written_num(96))
# print(written_num(117))
# print(written_num(475))
# print(written_num(400))
# print(written_num(707))

