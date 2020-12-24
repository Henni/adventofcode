import re

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


def solve():
    movements = readData()

    flipped = []

    switchMovement = {
        'w': lambda x,y: (x-1, y),
        'e': lambda x, y: (x+1, y),
        'nw': lambda x,y: (x-1,y-1),
        'ne': lambda x, y: (x, y-1),
        'sw': lambda x, y: (x, y+1),
        'se': lambda x, y: (x+1, y+1),
    }

    for move in movements:
        coord = (0,0)
        for m in move:
            coord = switchMovement[m](*coord)
            
        if coord in flipped:
            flipped.remove(coord)
        else:
            flipped.append(coord)
    
    return len(flipped)

if __name__ == "__main__":
    print(solve())
