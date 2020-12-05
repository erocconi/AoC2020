input = open("./input/d5.txt", "r").read().splitlines()
rows = [0,127]
seats = [0,7]
low = ['F','L']
high = ['B','R']
seatArr = []
#SUBTRACT ONE AT THE END

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

for i in input:
    rowRange = rows
    seatRange = seats
    for j in i[:7]:
        if type(rowRange) is list:
            rowRange = search(rowRange,j)
    for k in i[-3:]:
        if type(seatRange) is list:
            seatRange = search(seatRange,k)

    row = rowRange
    seat = seatRange
    seatId = (row*8)+seat
    seatArr.append(seatId)

seatArr = sorted(seatArr)
missing = missing_numbers(seatArr)

print(f'Part 1: {max(seatArr)}\nPart 2: {missing}')
