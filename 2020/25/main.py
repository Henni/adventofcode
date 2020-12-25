import re
from collections import defaultdict

def readData() -> list[list[int]]:
    with open('input.txt') as f:
        data = f.read()

    # parse
    data = data.split('\n')
    
    return [int(d) for d in data]

def transform(subject, loop):
    value = 1
    for _ in range(loop):
        value *= subject
        value %= 20201227
    return value

def transformStep(subject, value):
    return (value * subject % 20201227)

def findLoopSize(subject, goal):
    i = 0
    value = 1
    while value != goal:
        i += 1
        value = transformStep(subject, value)

    return i

def solve():
    data = readData()

    subject = 7

    loopSizes = [findLoopSize(subject, d) for d in data]

    print('Loop Sizes:', loopSizes)

    encryptionKey = transform(data[1], loopSizes[0])
    
    return encryptionKey

if __name__ == "__main__":
    print(solve())
