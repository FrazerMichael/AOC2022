#Advent of Code Day 2
#Michael Frazer

with open('rock_paper_scissors_input') as file:
    rpsThrows = []
    for each in file:
        rpsThrows.append(each.strip().split(' '))

#Part 1
def winner(opp = '', me = ''):
    myThrow = ''
    throwScore = 0

    if me == 'X':
        myThrow = 'A'
        throwScore += 1
    elif me == 'Y':
        myThrow = 'B'
        throwScore += 2
    else:
        myThrow = 'C'
        throwScore += 3

    if myThrow == opp:
        return 3, throwScore
    elif myThrow == 'A':
        if opp == 'B':
            return 0, throwScore
        else:
            return 6, throwScore
    elif myThrow == 'B':
        if opp == 'C':
            return 0, throwScore
        else:
            return 6, throwScore
    else:
        if opp == 'A':
            return 0, throwScore
        else:
            return 6, throwScore


#Part2

def throwCalculator(opp, result):
    if result == 'X':
        if opp == 'A':
            return 3
        elif opp == 'B':
            return 1
        else:
            return 2
    elif result == 'Y':
        if opp == 'A':
            return 4
        elif opp == 'B':
            return 5
        else:
            return 6
    else:
        if opp == 'A':
            return 8
        elif opp == 'B':
            return 9
        else:
            return 7


part1 = 0

for i in range(len(rpsThrows)):
    part1 += sum(winner(rpsThrows[i][0], rpsThrows[i][1]))

part2 = 0
test = []
for i in range(len(rpsThrows)):
    test.append(throwCalculator(rpsThrows[i][0], rpsThrows[i][1]))
    part2 += throwCalculator(rpsThrows[i][0], rpsThrows[i][1])

print('The answer for part 1:')
print(part1)

print('The answer for part 2:')
print(part2)
