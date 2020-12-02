import re

with open('input.txt') as f:
    data = f.readlines()

data = [d[:-1] for d in data]

# (min, max, char, password)
pattern = re.compile(
        r"(\d+)-(\d+) (\w): (\w+)"
        )

def parseLine(input):
    match = pattern.match(input)
    if not match:
        return None

    return match.groups()

def isValidPassword(data):
    count = data[3].count(data[2]) 
    return count >= int(data[0]) and count <= int(data[1]) 

def solve(input):
    # parse input
    input = map(parseLine, input)
    input = filter(isValidPassword, input)
    return len(list(input))

#print(solve(data))
