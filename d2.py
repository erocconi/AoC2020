with open("./input/d2.txt", "r") as inputFile:
    input = inputFile.read().splitlines()
    p1Count = 0
    p2Count = 0

    for i in input:
        x = i.split()
        ranges = x[0].split('-')
        letter = x[1][0]
        text = x[2]
        if text.count(letter) >= int(ranges[0]) and text.count(letter) <= int(ranges[1]):
            p1Count += 1
        if (text[(int(ranges[0])-1)] == letter) ^ (text[(int(ranges[1])-1)] == letter):
            p2Count += 1
    print(f"Part 1: {p1Count}\nPart 2: {p2Count}")