#AOC2022 Day 3
#Michael Frazer

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
            'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

with open('Rucksack_input') as file:
    rucksackCode = file.readlines()

filteredRucksack = []

for each in rucksackCode:
    filteredRucksack.append(each.strip())

def alphaValue(x):
    return alphabet.index(x) + 1

def duplicate(a, b):
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                return a[i]

count1 = 0

for each in filteredRucksack:
    splitPoint = int((len(each) + 1)/2)

    start = list(each[0:splitPoint])
    finish = list(each[splitPoint:])
    letter = duplicate(start, finish)

    count1 += alphaValue(letter)

count2 = 0

for i in range(0, len(filteredRucksack), 3):
    groupOfThree = filteredRucksack[i:i+3]
    listA = list(groupOfThree[0])
    listB = list(groupOfThree[1])
    listC = list(groupOfThree[2])

    firstPair = list(set(listA).intersection(listB))
    answer = list(set(listC).intersection(firstPair))

    count2 += alphaValue(answer[0])

print('Answer to Part 1:')
print(count1)

print('Answer to Part 2:')
print(count2)


