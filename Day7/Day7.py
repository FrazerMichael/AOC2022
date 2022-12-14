#Advent of Code Day 7
#Michael Frazer

import re

class Dir:
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent
        self.children = []
        self.data = []

with open('file_exploration') as file:
    messyInput = file.readlines()

cleanInput = [x[:-1] for x in messyInput]

root = Dir('root')
currentDirectory = root

allDirs = []
nDirs = []
nPlusOneDirs = []

def createDir(name, parent):
    globals()[name] = Dir(name, parent)
    allDirs.append(globals()[name])

for each in cleanInput:
    if each[2:4] == 'cd':
        if each[5:7] == '..':
            if currentDirectory is root:
                currentDirectory = currentDirectory.parent
            else:
                currentDirectory = globals()[currentDirectory].parent
        elif each[5:6] == '/':
            currentDirectory = root
        else:
            currentDirectory = each[5:]
    elif each[:3] == 'dir':
        createDir(each[4:], currentDirectory)
        if currentDirectory is root:
            currentDirectory.children.append(globals()[each[4:]])
        else:
            globals()[currentDirectory].children.append(globals()[each[4:]])
    elif each[0].isdigit():
        if currentDirectory is root:
            currentDirectory.data.append(int(re.findall("^\d*", each)[0]))
        else:
            globals()[currentDirectory].data.append(int(re.findall("^\d*", each)[0]))

    else:
        pass

size = 0

for each in allDirs:
    if len(each.children) == 0 and sum(each.data) <= 100000:
        nDirs.append(each)
        size += sum(each.data)

# for each in nDirs:
#     if sum(globals()[each.parent].data) <= 100000 - sum(each.data):
#         nPlusOneDirs.append(globals()[each.parent])

def legalParents(a):
    temp = []
    for each in a:
        if sum(globals()[each.parent].data) <= 100000 - sum(each.data):
            temp.append(globals()[each.parent])
    return temp

#Saving this as it was my first recursive code and I love it, but realized it was a silly way to approach this problem
def allChildren(a):
    temp = []
    if len(a.children) >= 1:
        for each in a.children:
            temp.append(each)
            temp += allChildren(each)
    return temp

def upAndCheck(a):
    temp = []
    for each in a:
        count = 0
        for i in allChildren(each):
            count += sum(i.data)
        if count <= 100000:
            print(count)
            temp.append(each)
    return temp

lvlOneUp = legalParents(nDirs)
lvlOneDown = upAndCheck(lvlOneUp)
print(lvlOneDown)
lvlTwoUp = legalParents(lvlOneUp)
lvlTwoDown = upAndCheck(lvlTwoUp)


print(lvlTwoDown)