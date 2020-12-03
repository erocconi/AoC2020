with open("./input/d1.txt", "r") as inputFile:
    input = inputFile.read().splitlines()
    for i in range(0, len(input)):
        input[i] = int(input[i])
    for item1 in input:
        for item2 in input:
            if (item1 + item2) == 2020:
                print("Part 1 == {}".format(item1*item2))
            for item3 in input:
                if (item1 + item2 + item3) == 2020:
                    print("Part 2 == {}".format(item1*item2*item3))