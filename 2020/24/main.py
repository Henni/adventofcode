import re
from collections import defaultdict

movePattern = re.compile(
    r'(w|e|nw|ne|sw|se)'
)

def readData() -> list[list[int]]:
    with open('input.txt') as f:
        data = f.read()

    # parse
    movements = data.split('\n')
    movements = [movePattern.findall(x) for x in movements]
    
    return movements


switchMovement = {
    'w': lambda x, y: (x-1, y),
    'e': lambda x, y: (x+1, y),
    'nw': lambda x, y: (x-1, y-1),
    'ne': lambda x, y: (x, y-1),
    'sw': lambda x, y: (x, y+1),
    'se': lambda x, y: (x+1, y+1),
}


def round(flipped):
    candidates = defaultdict(int)
    for x,y in flipped:
        neighbours = [f(x, y) for f in switchMovement.values()]
        for n in neighbours:
            if n not in flipped:
                candidates[n] += 1

    result = [c for c in flipped if
        sum([int(f(*c) in flipped) for f in switchMovement.values()]) in [1,2]
    ]

    result += [c for c,v in candidates.items() if v == 2]
        
    return result
            


def solve():
    movements = readData()

    flipped = []

    for move in movements:
        coord = (0,0)
        for m in move:
            coord = switchMovement[m](*coord)
            
        if coord in flipped:
            flipped.remove(coord)
        else:
            flipped.append(coord)

    for n in range(100):
        print(n)
        flipped = round(flipped)
    
    return len(flipped)

if __name__ == "__main__":
    print(solve())
