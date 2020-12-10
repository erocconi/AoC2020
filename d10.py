input = open("./input/d10.txt", "r").read().splitlines()
input = [0] + [int(item) for item in input]
sort = sorted(input)
voltDiff = []

for i in range(len(sort)-1):
    difference = sort[i+1] - sort[i]
    voltDiff.append(difference)

voltDiff.append(3)

part1 = voltDiff.count(1) * voltDiff.count(3)
print(f"Part 1: {part1}")
