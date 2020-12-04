input = open("./input/d4.txt", "r").read().splitlines()
passports = []
passport = {}
count,count2 = 0,0
items = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eyes = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

def validatePassport(pport):
    for k in items:
        if k in pport.keys():
            continue
        else:
            return False
    return True

def validatePart2(pport):
    if not (int(pport["byr"]) >= 1920 and int(pport["byr"]) <= 2002):
        return False
    if not (int(pport["iyr"]) >= 2010 and int(pport["iyr"]) <= 2020):
        return False
    if not (int(pport["eyr"]) >= 2020 and int(pport["eyr"]) <= 2030):
        return False
    height = pp["hgt"]
    if height[-2:] == "cm":
        if not (150 <= int(height[:-2]) <= 193):
            return False
    elif height[-2:] == "in":
        if not (59 <= int(height[:-2]) <= 76):
            return False
    else:
        return False
    hair = pp["hcl"]
    if hair[0] == '#':
        if not int(hair[1:], 16):
            return False
    else:
        return False
    if pp["ecl"] not in eyes:
        return False
    if len(pp["pid"]) != 9 or pp["pid"].isnumeric() == False:
        return False
    return True

for i in input:
    if not i:
        passports.append(passport)
        passport = {}
    else:
        for j in i.split(' '):
            j = j.split(':')
            passport[j[0]] = j[1]

for pp in passports:
    if validatePassport(pp) == True:
        count += 1
        if validatePart2(pp) == True:
            count2 += 1
            
print(f"Part 1: {count}\nPart 2: {count2}")