import math
import itertools
import time

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]

def nextBus(currentTime, busses: list[str]):

    fBusses = [int(b) for b in busses if b != 'x']

    nextDepartures = [(b, b - currentTime%b) for b in fBusses]
    print(nextDepartures)
    nextBus = min(*nextDepartures, key=lambda x: x[1])
    return math.prod(nextBus)

def solve(data: list[str]):
    currentTime = int(data[0])
    busses = data[1].split(',')

    print(nextBus(currentTime, busses))

    print('\nTask2:')
    
    # Valid Value Defintion
    fBusses = [(i,int(b)) for (i,b) in zip(range(len(busses)), busses) if b != 'x']
    print(fBusses)

    sortedBusses = list(reversed(sorted(fBusses, key=lambda a: a[1])))
    print(sortedBusses)
    #print(sieve(sortedBusses[0][1], sortedBusses[0][0], sortedBusses))

    value = sortedBusses[0][1] - sortedBusses[0][0] # a1 = i0
    step  = sortedBusses[0][1] # n1 = b0

    for j in sortedBusses[1:]:
        while True:
            print(value, value %j[1], j[1]-j[0])
            #time.sleep(1)
            if value % j[1] == (j[1] - j[0]) % j[1]:
                print(value)
                step *= j[1]
                break
            value += step

    print(value)




    # print(list(itertools.islice(numberGenerator(fBusses, 0), 10)))
    # for n in numberGenerator(fBusses, 0):
    #     valids = [int(validate(n, b, i)) for (i, b) in fBusses]
    #     if sum(valids) > 4:
    #         print(n, valids)
    #     #print([int(validate(n, b, i)) for (i,b) in fBusses])

def sieve(value, step, xs):
    if len(xs) == 1:
        return value
    while True:
        #                  b         prev i 
        if validate(value, xs[1][1], xs[0][0]):
            return sieve(value, step * xs[1][1], xs[1:])
        value += step


def validate(n, b, i):
    return (n + i) % b == 0

    # i = b - x % b
    # x % b = b - i
    # (x % b) - b + i = 0

def numberGenerator(fBusses, start):
    maxBus = max(*fBusses, key=lambda x:x[1])
    cur = (start % maxBus[1]) - maxBus[0]
    step = maxBus[1]

    while True:
        yield cur
        cur += step


if __name__ == "__main__":
    print(solve(data))
