from functools import reduce
import random

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]


def parseLine(input: str) -> tuple[int, int]:
    row = input[:7]
    col = input[7:]

    row = [int(r == 'B') for r in row]
    col = [int(c == 'R') for c in col]

    row = reduce(lambda x, y: (x << 1) + y, row)
    col = reduce(lambda x, y: (x << 1) + y, col)

    return (row, col)


def seatNumber(row: int, col: int) -> int:
    return row * 8 + col


def printSeats(seats: list[tuple[int, int]]):
    maxRow = 128
    maxCol = 8

    plan = [["  "] * maxCol for i in range(maxRow)]

    for s in seats:
        plan[s[0]][s[1]] = random.choice([
                u"\U0001F468",
                u"\U0001F469"
            ]) + random.choice([
                u"\U0001F3FB",
                u"\U0001F3FC",
                u"\U0001F3FD",
                u"\U0001F3FE",
                u"\U0001F3FF",
            ])

    printMatrix(transposeMatrix(plan))

def transposeMatrix(ls: list[int, int]) -> list[int, int]:
    transposed = [[0] * len(ls) for i in ls[0]]
    
    for i in range(len(ls)):
        for j in range(len(ls[i])):
            transposed[j][i] = ls[i][j]

    return transposed

def printMatrix(matrix):
    nRows = len(matrix)
    nCols = len(matrix[0])

    indent = len(str(nRows)) + 2

    # cols
    for i in reversed(range(len(str(nCols)))):
        out = [str(x // (10 ** i) % 10) for x in range(nCols)]

        print((" " * indent) + "  ".join(out))


    for i, row in enumerate(matrix):
        print(str(i).zfill(len(str(nRows))) + ": " + " ".join(row))

def solve(input):
    printSeats([parseLine(d) for d in input])


if __name__ == "__main__":
    print(solve(data))
