import re

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]

def parseInput(input: list[str]) -> list[list[str]]:
    # split passports
    splitList = [] # type: list[list[str]]
    splitStart = 0
    for i, v in enumerate(input+[""]): # append one line for last entry
        if v == "":
            splitList.append(input[splitStart:i])
            splitStart = i + 1

    return splitList

def chars():
    for c in range(ord('a'), ord('z')+1):
        yield c

def solve(input):
    data = parseInput(input)
    result = 0
    for group in data:
        for c in chars():
            if all([v.find(chr(c)) != -1 for v in group]):
                result += 1

    return result

if __name__ == "__main__":
    print(solve(data))
