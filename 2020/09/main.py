from typing import Set

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]

def isValid(cur, prev):
    for i, x in enumerate(prev):
        for y in prev[i+1:]:
            if x+y == cur:
                return True
    return False


def findError(data: list[int]):
    for i in range(25,len(data)):
        if not isValid(data[i], data[i-25:i]):
            return i, data[i]

def solve(input: list[int]):
    data = [int(x) for x in input]

    idx, value = findError(data)
    print(idx, value)

    for i in range(idx):
        for j in range(i+1,idx):
            if sum(data[i:j]) == value:
                return min(data[i:j-1]) + max(data[i:j-1])
            

if __name__ == "__main__":
    print(solve(data))
