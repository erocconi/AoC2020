input = open("./input/d5.txt", "r").read().splitlines()
rows = [0,127]
seats = [0,7]
low = ['F','L']
high = ['B','R']
seatIds = []

def missing_numbers(num_list):
      original_list = [x for x in range(num_list[0], num_list[-1] + 1)]
      num_list = set(num_list)
      return (list(num_list ^ set(original_list)))

def is_consecutive(l):
    setl = set(l)
    return len(l) == len(setl) and setl == set(range(min(l), max(l)+1))

def search(range,loc): 
    mid = (range[0] + range[1]) // 2

    if loc in low:
        newRange = [range[0],(mid)]
    elif loc in high:
        newRange = [(mid+1),range[1]]
    if is_consecutive(range):
        if loc in low:
            return newRange[0]
        elif loc in high:
            return newRange[1]
    else:
        return newRange

for boardingPass in input:
    rowRange = rows
    seatRange = seats
    for rowCode in boardingPass[:7]:
        rowRange = search(rowRange,rowCode)
    for seatCode in boardingPass[-3:]:
        seatRange = search(seatRange,seatCode)
    seatIds.append((rowRange*8)+seatRange)

part1 = max(seatIds)
part2 = missing_numbers(sorted(seatIds))[0]
print(f'Part 1: {part1}\nPart 2: {part2}')
