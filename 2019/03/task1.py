import sys

with open('input.txt') as f:
    data = f.readlines()[0:2]

wires = [d.split(',') for d in data]

def manhattan(coord):
    return abs(coord[0]) + abs(coord[1])

def shortest(coord, weightedWirePoints):
    return sum([l[coord] for l in weightedWirePoints])

# index wire points for wire 0
def getWirePoints(wire):
    coordinate = [0,0]
    wire_points = dict()
    strength = 0

    for strip in wire:
        direction = strip[0]
        length = int(strip[1:])

        if direction is 'U':
            for i in range(length):
                strength += 1
                wire_points[(coordinate[0], coordinate[1] + (i+1))] = strength
            coordinate[1] += length

        if direction is 'D':
            for i in range(length):
                strength += 1
                wire_points[(coordinate[0], coordinate[1] - (i+1))] = strength
            coordinate[1] -= length

        if direction is 'R':
            for i in range(length):
                strength += 1
                wire_points[(coordinate[0] + (i+1), coordinate[1])] = strength
            coordinate[0] += length

        if direction is 'L':
            for i in range(length):
                strength += 1
                wire_points[(coordinate[0] - (i+1), coordinate[1])] = strength
            coordinate[0] -= length

    return wire_points

def getIntersections(wirePoints):
    return wirePoints[0] & wirePoints[1]

weightedWirePoints = [getWirePoints(w) for w in wires]
wirePoints = [set(w.keys()) for w in weightedWirePoints]
intersections = getIntersections(wirePoints)
print(intersections)

closest = sorted(intersections, key=lambda x: shortest(x, weightedWirePoints))[0]
print(closest, shortest(closest, weightedWirePoints))
