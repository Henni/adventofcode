from pprint import pprint
from time import sleep

def readData() -> list[list[int]]:
    with open('input.txt') as f:
        data = f.read()

    # parse
    cups = [int(c) for c in data]

    return cups


class Ring:
    def __init__(self, list: list):
        self.list = list

    def __getitem__(self, val):
        if isinstance(val, slice):
            res = self.list[val.start:val.stop]
            if val.stop and val.stop > len(self.list):
                res += self.list[0:val.stop-len(self.list)]
            return Ring(res)
        else:
            return self.list[val]

    def __str__(self):
        return self.list.__str__()

    def index(self, val):
        return self.list.index(val)

    def __len__(self):
        return len(self.list)

    def __add__(self, other):
        return Ring(self.list + other.list)



def round(cups: Ring) -> Ring:
    current = cups[0] - 1  # we count current from zero
    selected = cups[1:4]
    remaining = cups[0:1]+cups[4:]

    print('--', current, selected)

    index = -1
    while index == -1:
        current = (current - 1) % len(cups)
        try:
            index = remaining.index(current+1)
        except ValueError:
            pass

    cups = remaining[:index+1] + selected + remaining[index+1:]
    cups = cups[1:] + cups[0:1]

    return cups


def solve():
    cups = readData()
    cups = Ring(cups)
    

    for _ in range(100):
        cups = round(cups)
        print(cups)

    oneIndex = cups.index(1)
    result = cups[oneIndex+1:oneIndex+len(cups)]

    return ''.join([str(x) for x in result])

if __name__ == "__main__":
    print(solve())
