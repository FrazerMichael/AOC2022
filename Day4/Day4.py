#Advent of Code Day 4
#Michael Frazer

firstClean = []
cleanPairs = []
intCleanPairs = []

with open('cleanup_input') as file:
    for each in file:
        firstClean.append(each.strip().split(','))

for i in range(len(firstClean)):
    temp = []
    for each in firstClean[i]:
        temp.append(each.split('-'))
    cleanPairs.append(temp)

for i in range(len(cleanPairs)):
    temp = []
    for j in cleanPairs[i]:
        temp2 = []
        for each in j:
            temp2.append(int(each))
        temp.append(temp2)
    intCleanPairs.append(temp)

def oneInTheOther(a):
    if a[0][0] >= a[1][0] and a[0][1] <= a[1][1]:
        return True
    elif a[0][0] <= a[1][0] and a[0][1] >= a[1][1]:
        return True
    else:
        return False

def belowThenIn (a):
    if a[0][0] < a[1][0] and a[0][1] >= a[1][0] and a[0][1] <= a[1][1]:
        return True
    elif a[0][0] > a[1][0] and a[0][0] <= a[1][1] and a[0][1] >= a[1][1]:
        return True
    else:
        return False

def inThenAbove (a):
    #print(a,a[0][0], a[1][0], a[0][0], )
    if a[0][0] >= a[1][0] and a[0][0] <= a[1][1] and a[0][1] > a[1][1]:
        print(a[0], a[1])
        return True
    elif a[1][0] >= a[0][0] and a[1][0] <= a[0][1] and a[1][1] > a[0][1]:
        return True
    else:
        return False


count = 0

for each in intCleanPairs:
    count += oneInTheOther(each)

count2 = 0

for each in intCleanPairs:
    print(count2)
    if oneInTheOther(each):
        count2 += 1
        continue
    elif belowThenIn(each):
        count2 += 1
        continue
    elif inThenAbove(each):
        count2 += 1
        continue
    else:
        continue
        



print('Answer for part 1:')
print(count)

print('Answer for part2:')
print(count2)


