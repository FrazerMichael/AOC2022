#Advent of Code Day 5
#Michael Frazer
import copy
import re

with open('crane_instructions') as file:
    fullInput = file.readlines()

craneInstructions = []

for each in fullInput[10:]:
    craneInstructions.append([int(s) for s in re.findall(r'\b\d+\b', each)])

supplyPilesP1 = [
    ['F', 'C', 'P', 'G', 'Q', 'R'],
    ['W', 'T', 'C', 'P'],
    ['B', 'H', 'P', 'M', 'C'],
    ['L', 'T', 'Q', 'S', 'M', 'P', 'R'],
    ['P', 'H', 'J', 'Z', 'V', 'G', 'N'],
    ['D', 'P', 'J'],
    ['L', 'G', 'P', 'Z', 'F', 'J', 'T', 'R'],
    ['N', 'L', 'H', 'C', 'F', 'P', 'T', 'J'],
    ['G', 'V', 'Z', 'Q', 'H', 'T', 'C', 'W']
]

supplyPilesP2 = copy.deepcopy(supplyPilesP1)

#Part 1
for each in craneInstructions:
    for i in range(each[0]):
        supplyPilesP1[each[2] - 1].append(supplyPilesP1[each[1] - 1].pop())

#Part 2
for each in craneInstructions:
    for i in range(-each[0], 0):
        supplyPilesP2[each[2] -1].append(supplyPilesP2[each[1] - 1].pop(i))


def topOfStacks(piles):
    topOfStacks  = ''
    for each in piles:
        topOfStacks += each[-1]
    return topOfStacks

print('Answer to Part 1:')
print(topOfStacks(supplyPilesP1))

print('Answer to Part 2:')
print(topOfStacks(supplyPilesP2))