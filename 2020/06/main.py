import re

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]

def parseInput(input: list[str]) -> list[dict[str,str]]:
    # split passports
    splitList = [] # type: list[list[str]]
    splitStart = 0
    for i, v in enumerate(input+[""]): # append one line for last entry
        if v == "":
            splitList.append(input[splitStart:i])
            splitStart = i + 1

    flattenedInput = ["".join(passport) for passport in splitList]

    return flattenedInput

def solve(input):
    return sum([len(set(v)) for v in parseInput(input)])

if __name__ == "__main__":
    print(solve(data))
