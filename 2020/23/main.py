def readData() -> list[list[int]]:
    with open('input.txt') as f:
        data = f.read()

    # parse
    cups = [int(c) for c in data]

    cups += range(10,1_000_001)

    cupDict = dict()
    for c in cups:
        cupDict[c] = Node(c)
        
    for c, next in zip(cups, cups[1:] + cups[0:1]):
        cupDict[c].next = cupDict[next]

    return cupDict, cupDict[cups[0]]

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def round(cupDict, cupHead: Node):
    current = cupHead.data
    selected = cupHead.next
    selectedValues = [selected.data, selected.next.data, selected.next.next.data]
    cupHead.next = selected.next.next.next
    cupHead = cupHead.next

    current = ((current - 2) % len(cupDict)) + 1
    while current in selectedValues:
        current = ((current - 2) % len(cupDict)) + 1

    selected.next.next.next = cupDict[current].next
    cupDict[current].next = selected

    return cupHead


def solve():
    cupDict, cupHead = readData()
    
    for i in range(10_000_000):
        if i % 100_000 == 0:
            print(i)
        cupHead = round(cupDict, cupHead)

    cup = cupDict[1]

    return cup.next.data * cup.next.next.data

if __name__ == "__main__":
    print(solve())
