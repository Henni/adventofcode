from copy import deepcopy
from enum import IntEnum
from pprint import pprint
import re

class Tile:
    def __init__(self, id: str, map: list[list[str]]) -> None:
        super().__init__()
        self.id = id
        self.map = map

    def getTop(self):
        return self.map[0]

    def getLeft(self):
        return list(reversed([x[0] for x in self.map]))

    def getRight(self):
        return [x[-1] for x in self.map]

    def getBottom(self):
        return list(reversed(self.map[-1]))

    def rotate(self, n=1):
        """
        only rotates outer clockwises
        """

        mapCopy = deepcopy(self.map)
        for _ in range(n):
            newMap = []
            for i in range(len(mapCopy)):
                newMap.append([x[i] for x in mapCopy[::-1]])
            mapCopy = newMap

        return Tile(self.id, mapCopy)

    def flipX(self):
        return Tile(self.id, [x[::-1] for x in self.map])
    
    def flipY(self):
        return Tile(self.id, [x.copy() for x in self.map[::-1]])

    def trim(self):
        return Tile(self.id, [x[1:-1] for x in self.map[1:-1]])
        


def readData() -> dict[str, Tile]:
    with open('input.txt') as f:
        data = f.read()

    # parse
    data = data.split('\n\n')
    data = [d.split('\n') for d in data]
    tiles = dict()
    for d in data:
        tileId = d[0][5:-1]
        tiles[tileId] = Tile(tileId, [list(x) for x in d[1:]])

    return tiles


def checkTile(x,y, selfBorder, selfDir, map, borders, tiles):
    if (x, y) not in map.keys():
        b = ''.join(selfBorder[::-1]) # reverse to match with opposite side

        if b in borders and len(borders[b]) == 1:
            dir, id, flipped = borders.pop(b)[0]

            removeIdFromBorders(borders, id)

            map[x,y] = tiles[id]
            if flipped and dir in [Direction.T, Direction.B]:
                map[x,y] = map[x,y].flipX()
            if flipped and dir in [Direction.L, Direction.R]:
                map[x,y] = map[x,y].flipY()

            map[x, y] = map[x, y].rotate((int(selfDir) - 2 - int(dir)) % 4)
            
            return {
                'x': x,
                'y': y,
            }
        else:
            return None
    return None   

def matchTiles(solved: list[dict[str,str]], tiles, map, borders: dict[str, str]):
    while len(solved) > 0:
        cur = solved[0]

        x = cur['x']
        y = cur['y']
        tile = map[x,y]

        # top
        t = checkTile(x, y-1, tile.getTop(), Direction.T, map, borders, tiles)
        if t != None:
            solved.append(t)
            
        # right
        t = checkTile(x+1, y, tile.getRight(), Direction.R, map, borders, tiles)
        if t != None:
            solved.append(t)
        
        # bottom
        t = checkTile(x, y+1, tile.getBottom(), Direction.B, map, borders, tiles)
        if t != None:
            solved.append(t)

        # left
        t = checkTile(x-1, y, tile.getLeft(), Direction.L, map, borders, tiles)
        if t != None:
            solved.append(t)

        # remove element from todos
        solved = solved[1:]

    return map


def removeIdFromBorders(borders, id):             # second spot in tuple
    newDic = {k:[x for x in v if x[1] != id] for (k, v) in borders.items()}
    newDic = {k:v for k,v in newDic.items() if len(v) > 0}

    borders.clear()
    borders |= newDic

class Direction(IntEnum):
    T = 0
    R = 1
    B = 2
    L = 3


def drawMap(map):
    coords = map.keys()

    maxX = max(x for x, _ in coords)
    minX = min(x for x, _ in coords)
    maxY = max(y for _, y in coords)
    minY = min(y for _, y in coords)

    for y in range(minY, maxY+1):
        for x in range(minX, maxX+1):
            if (x, y) in map:
                print(map[(x, y)].id, end=' ')
            else:
                print('    ', end=' ')
        print('')



def solve():
    tiles = readData()

    borders = dict()
    for t in tiles.values():
        for dir, x in [
            (Direction.T, t.getTop()),
            (Direction.B, t.getBottom()),
            (Direction.L, t.getLeft()),
            (Direction.R, t.getRight()),
        ]:
            # ignore duplicate borders for now
            key = ''.join(x)
            val = (dir, t.id, False)
            if key not in borders:
                borders[key] = [val]
            else:
                borders[key].append(val)

    flipped = {k[::-1]:[(dir, id, True) for (dir, id, _) in v]
        for k,v in borders.items()
    }

    for k,v in flipped.items():
        if k not in borders:
            borders[k] = v
        else:
            borders[k] += v

    startTile = {
        'x': 0,
        'y': 0,
    }

    startId = list(tiles.keys())[0]

    startMap = {
        (0,0): tiles[startId]
    }

    removeIdFromBorders(borders, startId)

    res = matchTiles([startTile], tiles, startMap, borders)

    drawMap(res)
    minX, minY = min(res)
    maxX, maxY = max(res)
    print('Task1: ',
        int(res[minX, minY].id) *
        int(res[minX, maxY].id) *
        int(res[maxX, minY].id) *
        int(res[maxX, maxY].id)
    )

    # print map
    printMap = []
    for y in range(minY, maxY+1):
        for iY in range(len(res[0, y].map)):
            printMap.append('')
            for x in range(minX, maxX+1):
                printMap[-1] += ''.join(res[x, y].map[iY]) + ' '
        printMap.append('')

    pprint(printMap, width=500)

    # trim overlap
    for y in range(minY, maxY+1):
        for x in range(minX, maxX+1):
            res[x,y] = res[x,y].trim()

    # merge map
    flatMap = []
    for y in range(minY, maxY+1):
        for iY in range(len(res[0,y].map)):
            flatMap.append([])
            for x in range(minX, maxX+1):
                flatMap[-1] += res[x,y].map[iY]

    rootTile = Tile('0', flatMap)

    maxSeamonsters = 0
    
    for r in range(3):
        # rotate, flipX, flipY
        # either X or Y flip suffices, combination is covered by rotation
        #print(r)
        x = countSeamonsters(rootTile.rotate(r))
        #print(x)
        maxSeamonsters = max(maxSeamonsters, x)
        x = countSeamonsters(rootTile.rotate(r).flipX())
        #print(x)
        maxSeamonsters = max(maxSeamonsters, x)
        x = countSeamonsters(rootTile.rotate(r).flipY())
        #print(x)
        maxSeamonsters = max(maxSeamonsters, x)
    
    seamonsterCharacters = 15
    totalSeamonsterChars = maxSeamonsters * seamonsterCharacters

    totalWaves = sum([x.count('#') for x in rootTile.map])
    print(totalWaves, maxSeamonsters)
    

    return totalWaves - totalSeamonsterChars

seaTop    = re.compile(r'..................#.')
seaMiddle = re.compile(r'#....##....##....###')
seaBottom = re.compile(r'.#..#..#..#..#..#...')

def countSeamonsters(tile: Tile):
    count = 0
    coords= []
    s = [''.join(x) for x in tile.map]
    for i in range(1, len(s)-1): # skip first and last
        offset = 0
        while True:
            search = seaMiddle.search(s[i],offset)

            if search != None:
                span = search.span()
                if (
                    seaTop.match(s[i-1],span[0], span[1]) != None and
                    seaBottom.match(s[i+1],span[0],span[1]) != None
                    ):
                    count += 1
                    coords += [
                        (offset+18, i-1), 
                        (offset+0, i+0), (offset+5, i), (offset+6, i), (offset+11, i),
                        (offset+12, i), (offset+17, i), (offset+18, i), (offset+19, i),
                        (offset+1, i+1), (offset+4, i+1), (offset+7, i+1), (offset+10, i+1),
                        (offset+13, i), (offset+16, i)
                    ]
                offset = span[0]+1
            else: break

    return count


if __name__ == "__main__":
    print(solve())
