from typing import NamedTuple

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]


class Movement(NamedTuple):  # pylint: disable=inherit-non-class
    command: str
    distance: int

def parseLine(data):
    return Movement(data[0], int(data[1:]))

DIRECTIONS = ['N', 'E', 'S', 'W']

# Coords:
# ^
# |
# + - >

class Ship:
    x: int
    y: int
    dir: str

    def __init__(self):
        self.x = 0
        self.y = 0
        self.dir = 'E'
    
    def act(self, m: Movement):
        if m.command in ['N','S','E','W','F']:
            self.move(m.command, m.distance)
        elif m.command in ['L', 'R']:
            self.rotate(m.command, m.distance)
        else:
            print("Unknown command!")
        
    def rotate(self, _dir: str, _degree: int):
        if _dir == 'R':
            self.dir = DIRECTIONS[(DIRECTIONS.index(self.dir) + _degree // 90) % len(DIRECTIONS)]
        if _dir == 'L':
            self.dir = DIRECTIONS[(DIRECTIONS.index(self.dir) - _degree // 90) % len(DIRECTIONS)]

    def move(self, _dir: str, _distance: int):
        if _dir == 'N' or _dir == 'F' and self.dir == 'N':
            self.y += _distance
            return
        if _dir == 'E' or _dir == 'F' and self.dir == 'E':
            self.x += _distance
            return
        if _dir == 'S' or _dir == 'F' and self.dir == 'S':
            self.y -= _distance
            return
        if _dir == 'W' or _dir == 'F' and self.dir == 'W':
            self.x -= _distance
            return

    def __str__(self) -> str:
        output = """
        (`-,-,
        ('(_,( )
        _   `_'
        __|_|__|_|_
    _|___________|__
    |o o o o o o o o/
    ~'`~'`~'`~'`~'`~'`~\n\n"""
        output += f"   X:   {self.x}\n"
        output += f"   Y:   {self.y}\n"
        output += f"   Dir: {self.dir}"
        return output

def solve(data):
    data = [parseLine(x) for x in data]

    ship = Ship()

    for m in data:
        ship.act(m)

    print(ship)
    print(abs(ship.x)+abs(ship.y))

if __name__ == "__main__":
    solve(data)
