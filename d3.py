with open("./input/d3.txt", "r") as inputFile:
    input = inputFile.read().splitlines()
    totalTrees = []
    paths = [
        [1,1],
        [3,1],
        [5,1],
        [7,1],
        [1,2]
        ]

    for path in paths:
        trees = 0
        xPos = 0
        for i in input[::path[1]]:
            if xPos > (len(i) -1):
                xPos = xPos - len(i)
            if i[xPos] == '#':
                trees += 1
                xPos += path[0]
            else:
                xPos += path[0]
        totalTrees.append(trees)
    finalTrees = 1
    for j in totalTrees:
        finalTrees = finalTrees * j
    print(f"Number of Trees: {finalTrees}")