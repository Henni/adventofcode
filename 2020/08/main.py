from typing import Set

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]


def parseLine(input):
    return input.split(" ")

def trySolve(input):
    visited = set()

    current = 0

    acc = 0

    while current not in visited and current < len(input):
        visited.add(current)
        [command, value] = parseLine(input[current])

        if command == 'acc':
            acc += int(value)
            current += 1
        elif command == 'jmp':
            current += int(value)
        else:
            current += 1
    
    # (acc value, finished)
    return acc, current >= len(input)

def solve(input: list[str]):
    for i in range(len(input)):
        curLine = parseLine(input[i])
        if curLine[0] == 'acc':
            continue

        fixedInput = input.copy()

        if curLine[0] == 'jmp':
            fixedInput[i] = 'nop ' + curLine[1]
        else:
            fixedInput[i] = 'jmp ' + curLine[1]

        acc, finished = trySolve(fixedInput)

        if finished:
            return acc

if __name__ == "__main__":
    print(solve(data))
