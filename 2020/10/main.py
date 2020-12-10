from typing import Set

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]

def solve(input):
    data = [int(x) for x in input]

    data.sort()

    diff = dict()

    for (prev, cur) in zip([0] + data,data + [data[-1]+3]):
        if cur-prev in diff.keys():
            diff[cur-prev] += 1
        else:
            diff[cur-prev] = 1

    print(diff)
    return diff[1] * diff[3]

if __name__ == "__main__":
    print(solve(data))
