input = open("./input/d1.txt", "r").read().splitlines()
for i in range(0, len(input)):
    input[i] = int(input[i])
for item1 in input:
    for item2 in input:
        if (item1 + item2) == 2020:
            print(f'Part 1: {(item1*item2)}')
        for item3 in input:
            if (item1 + item2 + item3) == 2020:
                print(f'Part 2: {(item1*item2*item3)}')