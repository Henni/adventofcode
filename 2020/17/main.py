import math

def readData():
    with open('input.txt') as f:
        data = f.read()
    
    # parse
    data = data.split('\n')
    data = [list(d) for d in data]

    return data

def isActive(w, l, y, x, prevData):
    w -= 1
    l -= 1
    y -= 1
    x -= 1

    wRange = range(
        max(w-1, 0),
        min(w+2, len(prevData))
    )

    lRange = range(
        max(l-1, 0),
        min(l+2, len(prevData[0]))
    )

    yRange = range(
        max(y-1, 0),
        min(y+2, len(prevData[0][0]))
    )

    xRange = range(
        max(x-1, 0),
        min(x+2, len(prevData[0][0][0]))
    )

    

    actives = 0
    for _w in wRange:
        for _l in lRange:
            for _y in yRange:
                for _x in xRange:
                    if prevData[_w][_l][_y][_x] == '#':
                        actives += 1

    if w in wRange and l in lRange and y in yRange and x in xRange and prevData[w][l][y][x] == '#':
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
        [
            ['.'] * (len(data[0][0])+2)
            for _ in range(len(data[0][0])+2)
        ]
        for _ in range(len(data[0])+2)
        ]
        for _ in range(len(data)+2)
    ]


    for w, wDim in enumerate(newData):
        for l, layer in enumerate(wDim):
            for y, row in enumerate(layer):
                for x in range(len(row)):
                    newData[w][l][y][x] = '#' if isActive(w, l, y, x, data) else '.'

    return newData

def solve():
    data = readData()
    data = [[data]]
    
    for _ in range(6):
        data = step(data)

    actives = [x for w in data for layer in w for row in layer for x in row].count('#')
    return actives

if __name__ == "__main__":
    print(solve())
