from collections import Counter 

input = open("./input/d6.txt", "r").read().splitlines()
part1 = []
part2 = []
answer = set()
answerGroup = []
for i in input:
    if not i:
        part1.append(len(answer))
        groupAnswers_copy = groupAnswers = list("".join(answerGroup))
        for group in answerGroup:
            number = len(answerGroup)
            for j in set(groupAnswers_copy):
                if Counter(groupAnswers_copy)[j] != number:
                    groupAnswers = [v for v in groupAnswers if v != j]
        part2.append(len(set(groupAnswers)))
        answerGroup = []
        answer = set()
    else:
        answer.update(i)
        answerGroup.append(i)

part1a = 0
for count1 in part1:
    part1a = part1a + count1
part2a = 0
for count2 in part2:
    part2a = part2a + count2
print(f'Part1: {part1a}\nPart2: {part2a}')