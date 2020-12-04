input = open("./input/d3.txt", "r").read().splitlines()
totalTrees = []
paths = [[1,1],[3,1],[5,1],[7,1],[1,2]]

for xMove, yMove in paths:
    trees, xPos = 0, 0
    for i in input[::yMove]:
        if xPos > (len(i) -1):
            xPos = xPos - len(i)
        if i[xPos] == '#':
            trees += 1
        xPos += xMove
    totalTrees.append(trees)
finalTrees = 1
for j in totalTrees:
    finalTrees = finalTrees * j
print(f"Number of Trees: {finalTrees}")