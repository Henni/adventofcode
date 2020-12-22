from pprint import pprint
from time import sleep

def readData() -> list[list[int]]:
    with open('input.txt') as f:
        data = f.read()

    # parse
    decks = data.split('\n\n')
    decks = [d.split('\n')[1:] for d in decks]
    decks = [[int(c) for c in d] for d in decks]

    return decks


def solve():
    decks = readData()

    while all([len(x)>0 for x in decks]):
        a = decks[0].pop(0)
        b = decks[1].pop(0)
        #print(a,b)

        if a > b:
            decks[0].extend([a, b])
        else:
            decks[1].extend([b, a])

    winner = max([0,1], key=lambda x: len(decks[x]))

    print('Winner: ', winner)

    score = 0

    for i,v in enumerate(decks[winner][::-1]):
        score += (i+1) * v

    return score

if __name__ == "__main__":
    print(solve())
