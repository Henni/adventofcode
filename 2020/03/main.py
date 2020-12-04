import re

with open('input.txt') as f:
    data = f.readlines()

data = [d[:-1] for d in data]

def isTree(slope, x,y):
    return slope[y][x%len(slope[0])] == "#"
    
def runSlope(slope, xInc, yInc):
    x = 0
    y = 0
    numTrees = 0
    while y < len(slope):
        if isTree(slope, x,y):
            numTrees += 1
        x += xInc
        y += yInc

    return numTrees

def solve(slope):
    return (
            runSlope(slope, 1, 1)
          * runSlope(slope, 3, 1)
          * runSlope(slope, 5, 1)
          * runSlope(slope, 7, 1)
          * runSlope(slope, 1, 2)
          )

if __name__ == "__main__":
    print(solve(data))
