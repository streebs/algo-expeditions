def alphabetize():
    with open('euler/inputs/22_names.txt', 'r') as file:
        data = file.read()

    data = data.split(',')
    data = [s.strip('"') for s in data]
    data = sorted(data)

    return data

def get_name_score(name):
    sum = 0
    for char in name:
        sum += (ord(char) - 64)
    return sum

def name_scores():
    data = alphabetize()
    sum = 0
    for i in range(len(data)):
        sum += (get_name_score(data[i]) * (i+1))

    return sum

print(name_scores())

# print(get_name_score('COLIN'))