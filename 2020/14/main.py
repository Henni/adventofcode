import math
import re

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]


def updateMask(memory, _, line):
    return memory, line.split(' ')[-1]

def applyMask(x: int, mask: str):
    x = x | int(mask.replace('X', '0'), 2) # apply 1 mask
    x = x & int(mask.replace('X', '1'), 2) # apply 0 mask
    return x


memPattern = re.compile(
    r'mem\[(\d+)\] = (\d+)'
)

def updateMem(memory, mask, line: str):
    print(line)
    i, x = memPattern.match(line).groups()
    x = applyMask(int(x), mask)
    memory[i] = x
    return memory, mask


def solve(data: list[str]):
    memory = {}
    mask = "0"
    for d in data:
        if d.startswith('mask'):
            memory, mask = updateMask(memory, mask, d)
        else:
            memory, mask = updateMem(memory, mask, d)

    return sum(memory.values())



if __name__ == "__main__":
    print(solve(data))
