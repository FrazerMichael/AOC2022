#Advent of Code Day 2
#Michael Frazer

with open('rock_paper_scissors_input') as file:
    rpsThrows = []
    for each in file:
        rpsThrows.append(each.strip().split(' '))

def winner(opp, me):
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

total = 0

for i in range(len(rpsThrows)):
    total += sum(winner(rpsThrows[i][0], rpsThrows[i][1]))

print('The answer for part 1:')
print(total)