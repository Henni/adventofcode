import itertools

data = [0, 3, 1, 6, 7, 5]

def generateNum(data: list[str]):
    latestIndex = {}
    i = 0
    for i, d in enumerate(data):
        latestIndex[d] = i
        yield d

    i = len(data)
    while True:
        if not data[-1] in latestIndex.keys():
            x = 0
        else:
            x = (i - 1) - latestIndex[data[-1]]
        latestIndex[data[-1]] = i - 1
        data.append(x)
        yield x
        i += 1

def solve(data):
    n = 30000000
    return next(itertools.islice(generateNum(data),n-1, n))



if __name__ == "__main__":
    print(solve(data))
