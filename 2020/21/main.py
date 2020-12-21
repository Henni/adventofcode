from pprint import pprint

def readData():
    with open('input.txt') as f:
        data = f.read()

    # parse
    data = data.split('\n')
    foods = []
    for f in data:
        ingredients, allergenes = f.split(' (contains ')
        ingredients = ingredients.split(' ')
        allergenes = allergenes[:-1].split(', ')

        foods.append((ingredients, allergenes))

    return foods


def solve():
    foods = readData()

    possAler = dict()

    allAler = set()
    allAler.update(*[f[1] for f in foods])

    allIng = set()
    allIng.update(*[f[0] for f in foods])

    possAler = {k:allIng.copy() for k in allAler}

    for ing, aler in foods:
        for a in aler:
            possAler[a] = possAler[a].intersection(ing)

    possIng = set()
    possIng.update(*possAler.values())

    noAler = allIng.difference(possIng)

    res = 0

    for ing, _ in foods:
        for x in noAler:
            res += ing.count(x)

    print('Task 1:', res)

    # Find solved and clean others
    solved = dict()
    while len(possAler) > 0:
        for k,v in possAler.items():
            if len(v) == 1:
                x = possAler[k].pop()
                solved[k] = x
                for k1 in possAler:
                    possAler[k1].discard(x)

        
        possAler = {k:v for k,v in possAler.items() if len(v) > 0}

    return ','.join([solved[x] for x in sorted(allAler)])

if __name__ == "__main__":
    print(solve())
