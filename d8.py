import copy
input = list([l.split() for l in open("./input/d8.txt", "r")])

acc = 0
posArr = []

def executeBoot(data,loc=0):
    global acc, posArr
    if loc == len(data):
        return True
    elif loc in posArr:
        return False
    else:
        posArr.append(loc)
        operation, instruction = data[loc]
        if operation == 'jmp':
            newPos = loc + int(instruction)
        elif operation == 'acc':
            acc += int(instruction)
            newPos = loc + 1
        elif operation == 'nop':
            newPos = loc + 1   
        return executeBoot(data,newPos)

if not executeBoot(input):
    Part1 = acc
for i in range(len(input)):
    acc = 0
    posArr = []
    input_copy = copy.deepcopy(input)
    if input_copy[i][0] == 'nop':
        input_copy[i][0] = 'jmp'
    elif input_copy[i][0] == 'jmp':
        input_copy[i][0] = 'nop'
    else:
        continue
    if executeBoot(input_copy):
        Part2 = acc

print(f'Part 1: {Part1}\nPart 2: {Part2}')