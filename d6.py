input = open("./input/d6.txt", "r").read().splitlines()
answers = []
answer = set()
for i in input:
    if not i:
        answers.append(len(answer))
        answer = set()
    else:
        for j in i:
            answer.update(j)

finalCount = 0
for count in answers:
    finalCount = finalCount + count

print(f'Part1: {finalCount}')

"""     output = set()
    for line in input:
        words = line.split()
        output.update(words) """