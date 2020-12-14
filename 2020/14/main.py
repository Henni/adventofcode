import math
import re

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]


def updateMask(memory, _, line):
    return memory, line.split(' ')[-1]


def generateMasks(mask: str):
    masks = [mask.replace('0', ' ').replace('1', ' ')]
    idx = -1
    Xs = [i for i in range(len(mask)) if mask[i] == 'X']
    for idx in Xs:
        newMasks = []
        for m in masks:
            if idx == len(mask) - 1:
                newMasks += [
                    m[:idx] + '0',
                    m[:idx] + '1',
                ]
            else:
                newMasks += [
                    m[:idx] + '0' + m[idx+1:],
                    m[:idx] + '1' + m[idx+1:],
                ]
        masks = newMasks
    return masks

def applyMask(x: int, mask: str):
    masks = generateMasks(mask)
    values = []
    for m in masks:
        value = x |  int(mask.replace('X', '0'), 2) # 1s
        value = value | int(m.replace(' ', '0'), 2) # 1 Xs
        value = value & int(m.replace(' ', '1'), 2) # 0 Xs
        values.append(
            value
        )
    
    return values


memPattern = re.compile(
    r'mem\[(\d+)\] = (\d+)'
)

def updateMem(memory, mask, line: str):
    i, x = memPattern.match(line).groups()
    ids = applyMask(int(i), mask)
    for id in ids:
        memory[id] = x
    return memory, mask


def solve(data: list[str]):
    memory = {}
    mask = "0"
    for d in data:
        if d.startswith('mask'):
            memory, mask = updateMask(memory, mask, d)
        else:
            memory, mask = updateMem(memory, mask, d)

    return sum([int(x) for x in memory.values()])



if __name__ == "__main__":
    print(solve(data))
