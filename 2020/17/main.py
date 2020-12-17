import math

def readData():
    with open('input.txt') as f:
        data = f.read()
    
    # parse
    data = data.split('\n')
    data = [list(d) for d in data]

    return data

def isActive(l, y, x, prevData):
    l -= 1
    y -= 1
    x -= 1

    lRange = range(
        max(l-1, 0),
        min(l+2, len(prevData))
    )

    yRange = range(
        max(y-1, 0),
        min(y+2, len(prevData[0]))
    )

    xRange = range(
        max(x-1, 0),
        min(x+2, len(prevData[0][0]))
    )

    actives = 0
    for _l in lRange:
        for _y in yRange:
            for _x in xRange:
                if prevData[_l][_y][_x] == '#':
                    actives += 1

    if l in lRange and y in yRange and x in xRange and prevData[l][y][x] == '#':
        return (actives - 1) in [2,3]
    else:
        return actives in [3]

def printData(data):
    for layer in data:
        for row in layer:
            print(''.join([str(r) for r in row]))
        print('')

def step(data):
    newData = [
        [
            ['.'] * (len(data[0])+2)
            for _ in range(len(data[0])+2)
        ]
        for _ in range(len(data)+2)
    ]

    for l, layer in enumerate(newData):
        for y, row in enumerate(layer):
            for x in range(len(row)):
                newData[l][y][x] = '#' if isActive(l, y, x, data) else '.'

    return newData

def solve():
    data = readData()
    data = [data]
    
    for _ in range(6):
        data = step(data)

    actives = [x for layer in data for row in layer for x in row].count('#')
    return actives

if __name__ == "__main__":
    print(solve())
