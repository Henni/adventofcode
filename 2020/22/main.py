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

def calculateScore(winner, decks):
    print('Winner: ', winner)

    score = 0

    for i,v in enumerate(decks[winner][::-1]):
        score += (i+1) * v

    return score


def game(decks) -> int:
    played = []

    while all([len(x) > 0 for x in decks]):
        if decks in played:
            return 0
        
        played.append([decks[0].copy(), decks[1].copy()])
        a = decks[0].pop(0)
        b = decks[1].pop(0)

    
        if a <= len(decks[0]) and b <= len(decks[1]):
            roundWinner = game([
                decks[0][:a].copy(),
                decks[1][:b].copy()
            ]) #recurse
            decks[roundWinner].append([a,b][roundWinner])
            decks[roundWinner].append([b,a][roundWinner])

        else:
            if a > b:
                decks[0].extend([a, b])
            else:
                decks[1].extend([b, a])

    return max([0, 1], key=lambda x: len(decks[x]))


def solve():
    decks = readData()

    winner = game(decks)
    print(decks)

    return calculateScore(winner, decks)

if __name__ == "__main__":
    print(solve())
