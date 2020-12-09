from typing import Set

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]

def isValid(cur, prev):
    for i, x in enumerate(prev):
        for y in prev[i+1:]:
            if x+y == cur:
                return True
    return False


def solve(input: list[str]):
    data = [int(x) for x in input]

    for i in range(25,len(input)):
        if not isValid(data[i], data[i-25:i]):
            return data[i]

if __name__ == "__main__":
    print(solve(data))
