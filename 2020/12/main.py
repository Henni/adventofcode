from typing import NamedTuple

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]


class Movement(NamedTuple):  # pylint: disable=inherit-non-class
    command: str
    distance: int

def parseLine(data):
    return Movement(data[0], int(data[1:]))

DIRECTIONS = ['N', 'E', 'S', 'W']

class Waypoint:
    x: int
    y: int

    def __init__(self):
        self.x = 10
        self.y = 1

    def move(self, _dir: str, _distance: int):
        if   _dir == 'N': self.y += _distance
        elif _dir == 'E': self.x += _distance
        elif _dir == 'S': self.y -= _distance
        elif _dir == 'W': self.x -= _distance
        else: print('Unknown direction')
    
    def rotate(self, _dir: str, _degree: int):
        normalized = _degree if _dir == 'R' else 360 - _degree
        normalized %= 360
        if   normalized == 90:
            self.x, self.y =  self.y, -self.x
        elif normalized == 180:
            self.x, self.y = -self.x, -self.y
        elif normalized == 270:
            self.x, self.y = -self.y,  self.x

# Coords:
# ^
# |
# + - >

class Ship:
    x: int
    y: int
    dir: str
    waypoint: Waypoint

    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint = Waypoint()
    
    def act(self, m: Movement):
        if   m.command in ['F']:
            self.move(m.distance)
        elif m.command in ['N','S','E','W']:
            self.waypoint.move(m.command, m.distance)
        elif m.command in ['L', 'R']:
            self.waypoint.rotate(m.command, m.distance)
        else:
            print("Unknown command!")

    def move(self, _distance: int):
        self.x += _distance * self.waypoint.x
        self.y += _distance * self.waypoint.y

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
