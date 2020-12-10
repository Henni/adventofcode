from typing import Set

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]

def isValid(low, high, data):
    for (prev, cur) in zip([low] + data, data + [high]):
        if (cur - prev) > 3:
            return False

    return True

def recurse(low, high, data):
    valids = 0
    for i in range(len(data)-1):
        cur = data[:i] + data[i+1:]
        if isValid(low, high, cur):
            valids += 1 + recurse(low, high, cur)

    return valids

def solve(input):
    data = [int(x) for x in input]

    data.sort()

    return recurse(0, data[-1]+3, data)

if __name__ == "__main__":
    print(solve(data))
