#Advent of Code Day 6
#Michael Frazer

with open('radio_input') as file:
    radioInput = list(file.read())

print(len(radioInput))

#part 1
for i in range(len(radioInput)):
    first = radioInput[i]
    second = radioInput[i+1]
    third = radioInput[i+2]
    fourth = radioInput[i+3]
    if first in [second, third, fourth]:
        continue
    if second in [third, fourth]:
        continue
    if third in fourth:
        continue
    else:
        print('Answer to Part 1:')
        print(i+4)
        break

#part 2
temp = []
for i in range(len(radioInput)):
    if radioInput[i] in temp:
        temp = [radioInput[i]]
        continue
    else:
        temp.append(radioInput[i])
        if len(temp) == 14:
            print(temp)
            print('Answer to Part 2:')
            print(i + 1)
            break