import math

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]

def solve(data: list[str]):
    currentTime = int(data[0])
    busses = data[1].split(',')

    busses = [int(b) for b in busses if b != 'x']

    nextDepartures = [(b, b - currentTime%b) for b in busses]
    print(nextDepartures)
    nextBus = min(*nextDepartures, key=lambda x: x[1])
    return math.prod(nextBus)

if __name__ == "__main__":
    print(solve(data))
