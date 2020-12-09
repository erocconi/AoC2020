input = open("./input/d9.txt", "r").read().splitlines()
input = [int(item) for item in input]

def compare(data,loc):
    last25 = data[loc:(loc+25)]
    current = data[(loc+25)]
    for i in last25:
        for j in last25:
            if i + j == current:
                return True
    return False

for number in range(len(input)):
    if compare(input,number) is not True:
        part1 = input[number+25]
        break

for number in range(len(input)):
    for i in range(number+1, len(input)):
        array = input[number:i]
        if sum(array) == part1:
            part2 = min(array)+max(array)
            print(f'Day 9\nPart 1: {part1}\nPart 2: {part2}')
            exit() # Gets two answers if I don't exit???