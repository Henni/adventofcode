from copy import deepcopy
from enum import IntEnum


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
        print('Coord: ', x, y)
        b = ''.join(selfBorder[::-1]) # reverse to match with opposite side

        if b in borders and len(borders[b]) == 1:
            dir, id, flipped = borders.pop(b)[0]
            print('Id:    ', id)

            removeIdFromBorders(borders, id)

            map[x,y] = tiles[id].rotate((int(selfDir) - 2 - int(dir)) % 4)
            if flipped and dir in [Direction.T, Direction.B]:
                map[x,y] = map[x,y].flipX()
            if flipped and dir in [Direction.L, Direction.R]:
                map[x,y] = map[x,y].flipY()
            
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

    drawMap(tiles, res)

    minX, minY = min(res)
    maxX, maxY = max(res)
    return (
        int(res[minX, minY].id) *
        int(res[minX, maxY].id) *
        int(res[maxX, minY].id) *
        int(res[maxX, maxY].id)
    )


def drawMap(tiles, map):
    coords = map.keys()

    maxX = max(x for x,_ in coords)
    minX = min(x for x,_ in coords)
    maxY = max(y for _,y in coords)
    minY = min(y for _,y in coords)

    for y in range(minY, maxY+1):
        for x in range(minX, maxX+1):
            if (x,y) in map:
                print(map[(x,y)].id, end=' ')
            else:
                print('    ', end=' ')
        print('')


if __name__ == "__main__":
    print(solve())
