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

    #pprint(possAler)
    
    #for ing, aler in foods:
    #    for a in allAler.difference(aler):
    #        print(a, ing)
    #        possAler[a].difference_update(set(ing))

    noAler = allIng.difference(possIng)

    res = 0

    for ing, _ in foods:
        for x in noAler:
            res += ing.count(x)

    return res


if __name__ == "__main__":
    pprint(solve())
