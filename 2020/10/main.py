import math

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]

def findGroups(low, high, data):
    groupStart = 0
    groups = []

    prevs = [low] + data
    currs = data + [high]
    for i in range(len(data) + 1):
        if (currs[i] - prevs[i]) == 3:
            groups.append(prevs[groupStart:i+1])
            groupStart = i+1

    return groups

def combinations(i):
    return [0, 1, 1, 2, 4, 7, 0][i]

def solve(input):
    data = [int(x) for x in input]
    data.sort()

    groups = findGroups(0, data[-1]+3, data)
    combs = [combinations(len(x)) for x in groups]
    return math.prod(combs)

if __name__ == "__main__":
    print(solve(data))
