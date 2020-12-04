input = open("./input/d2.txt", "r").read().splitlines()
p1Count = 0
p2Count = 0

for i in input:
    ranges, letter, text = i.split()
    lower, upper = ranges.split('-')
    letter = letter[0]
    if text.count(letter) >= int(lower) and text.count(letter) <= int(upper):
        p1Count += 1
    if (text[(int(lower)-1)] == letter) ^ (text[(int(upper)-1)] == letter):
        p2Count += 1
print(f"Part 1: {p1Count}\nPart 2: {p2Count}")