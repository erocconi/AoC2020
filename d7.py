import re
import collections

input = open("./input/d7.txt", "r").read().splitlines()
myBag = 'shiny gold'
heldIn = collections.defaultdict(list)
holds = collections.defaultdict(list)
totalBags = []

def crawl_up(color):
    for bag in heldIn[color]:
        totalBags.append(bag)
        crawl_up(bag)

def crawl_down(color):
    InMyBag = 0
    for number, bagColor in holds[color]:
        InMyBag += int(number)
        InMyBag += int(number) * crawl_down(bagColor)
    return InMyBag

for i in input:
    bagColor = ' '.join(i.split(' ')[:2])
    for number, color in re.findall(r'(\d+) (.+?) bags?[,.]', i):
        bagData = (number,color)
        heldIn[color].append(bagColor)
        holds[bagColor].append(bagData)

crawl_up(myBag)
part2 = crawl_down(myBag)
part1 = len(set(totalBags))
print(f'Part 1: {part1}\nPart 2: {part2}')