import re
from typing import Set

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]


def parseLine(input):
    return input.split(" ")

def solve(input):
    visited = set()

    current = 0

    acc = 0

    while current not in visited:
        visited.add(current)
        [command, value] = parseLine(input[current])

        if command == 'acc':
            acc += int(value)
            current += 1
        elif command == 'jmp':
            current += int(value)
        else:
            current += 1
    
    return acc

if __name__ == "__main__":
    print(solve(data))
