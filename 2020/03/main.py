import re

with open('input.txt') as f:
    data = f.readlines()

data = [d[:-1] for d in data]

def isTree(x,y):
    return data[y][x%len(data[0])] == "#"
    
def solve(input):
    x = 0
    y = 0
    numTrees = 0
    while y < len(input):
        if isTree(x,y):
            numTrees += 1
        x += 3
        y += 1

    return numTrees

if __name__ == "__main__":
    print(solve(data))
