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

def isValid(passport: dict[str, str]) -> bool:
    if all([requiredField in passport.keys() for requiredField in requiredFields]):
        print(passport)
        return True
    return False

def solve(input):
    passports = parseInput(input)
    validPassports = [passport for passport in passports if isValid(passport)]
    return len(validPassports)


if __name__ == "__main__":
    print(solve(data))
