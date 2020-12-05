import re

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]

def parseInput(input: list[str]) -> list[dict[str,str]]:
    # split passports
    splitList = [] # type: list[list[str]]
    splitStart = 0
    for i, v in enumerate(input+[""]): # append one line first last entry
        if v == "":
            splitList.append(input[splitStart:i])
            splitStart = i + 1
    
    print("Passports found: ", len(splitList))

    flattenedPassports = [" ".join(passport) for passport in splitList]
    passportStringList = [passport.split(" ") for passport in flattenedPassports]
    passportTupleList = [[tuple(entry.split(":")) for entry in passport] for passport in passportStringList]
    passportDictList = [dict(passport) for passport in passportTupleList]

    return passportDictList


# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID)
requiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

# hcl regex
hclPattern = re.compile(
    r"#[0-9a-f]{6}$"
)

# ecl allowed entries
eclAllowed = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

# pid regex
pidPattern = re.compile(
    r"\d{9}$"
)

def isValid(passport: dict[str, str]) -> bool:
    # early escape
    if not all([requiredField in passport.keys() for requiredField in requiredFields]):
        return False

    if not all([p in requiredFields + ['cid'] for p in passport.keys()]):
        return False
    
    print(passport)
    # byr (Birth Year)
    byr = int(passport['byr'])
    if not 1920 <= byr <= 2002:
        print('byr')
        return False
    
    # iyr (Issue Year)
    iyr = int(passport['iyr'])
    if not 2010 <= iyr <= 2020:
        print('iyr')
        return False

    # eyr (Expiration Year)
    eyr = int(passport['eyr'])
    if not 2020 <= eyr <= 2030:
        print('eyr')
        return False
    
    # hgt (Height)
    hgt = passport['hgt']
    if len(hgt) < 2:
        return False
    unitHgt = hgt[-2:]
    intHgt = int(hgt[:-2])
    if unitHgt == "cm":
        if not 150 <= intHgt <= 193:
            return False
    elif unitHgt == "in":
        if not 59 <= intHgt <= 76:
            return False
    else:
        return False

    # hcl (Hair Color)
    hcl = passport['hcl']
    if not hclPattern.match(hcl):
        print('hcl')
        return False

    # ecl (Eye Color)
    ecl = passport['ecl']
    if not ecl in eclAllowed:
        print('ecl')
        return False
    
    # pid (Passport ID)
    pid = passport['pid']
    if not pidPattern.match(pid):
        print('pid')
        return False

    #print('fine....')
    return True

def solve(input):
    passports = parseInput(input)
    validPassports = [passport for passport in passports if isValid(passport)]
    return len(validPassports)


if __name__ == "__main__":
    print(solve(data))
