from functools import reduce

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


def solve(input) -> None:
    return max(*[seatNumber(*parseLine(d)) for d in input])


if __name__ == "__main__":
    print(solve(data))
