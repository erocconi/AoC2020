input = open("./input/d4.txt", "r").read().splitlines()
passports = []
passport = {}
count,count2 = 0,0
items = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
eyes = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

def validatePassport(pport):
    for k in items:
        if k in pport.keys():
            continue
        else:
            return False
    return True

def validatePart2(pport):
    if not (1920 <= int(pport["byr"]) <= 2002):
        return False
    if not (2010 <= int(pport["iyr"]) <= 2020):
        return False
    if not (2020 <= int(pport["eyr"]) <= 2030):
        return False
    if pport["hgt"][-2:] == "cm":
        if not (150 <= int(pport["hgt"][:-2]) <= 193):
            return False
    elif pport["hgt"][-2:] == "in":
        if not (59 <= int(pport["hgt"][:-2]) <= 76):
            return False
    else:
        return False
    if pport["hcl"][0] == '#':
        if not int(pport["hcl"][1:], 16):
            return False
    else:
        return False
    if pport["ecl"] not in eyes:
        return False
    if len(pport["pid"]) != 9 or pport["pid"].isnumeric() == False:
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