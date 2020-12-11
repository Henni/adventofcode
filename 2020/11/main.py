from curses import wrapper
import curses

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]


def main(stdscr):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_BLACK)
    # Clear screen
    stdscr.clear()

    # This raises ZeroDivisionError when i == 10.
    solve(stdscr, data)

    stdscr.refresh()
    stdscr.getkey()


def transpose(ls: list[str]) -> list[str]:
    transposed = [[0] * len(ls) for i in ls[0]]

    for i in range(len(ls)):
        for j in range(len(ls[i])):
            transposed[j][i] = ls[i][j]

    return transposed

def draw(stdscr, data: list[str], counter):
    (height, width) = stdscr.getmaxyx()
    for y in range(min(len(data), height)):
        for x in range(min(len(data[0]), height)):
            if data[y][x] == '#':
                stdscr.addstr(y, x, data[y][x], curses.color_pair(1))
            elif data[y][x] == '.':
                stdscr.addstr(y, x, data[y][x], curses.color_pair(2))
            elif data[y][x] == 'L':
                stdscr.addstr(y, x, data[y][x], curses.color_pair(3))
            else:
                stdscr.addstr(y, x, data[y][x])

    stdscr.addstr(2, width-10, str(counter))
    
    stdscr.refresh()

def neighbours(data, x, y):
    n = 0
    for a, i in enumerate(range(x-1,x+2)):
        if not 0 <= i < len(data[0]): continue
        for b, j in enumerate(range(y-1,y+2)):
            if a == 1 and b == 1: continue
            if not 0 <= j < len(data): continue
            if data[j][i] == '#':
                n += 1
    return n

def newOccupation(data, x, y):
    if data[y][x] == '#':
        if neighbours(data, x, y) >= 4:
            return 'L'
    elif data[y][x] == 'L':
        if neighbours(data, x, y) == 0:
            return '#'
    
    return data[y][x]

def neighbourTable(input, empty):
    next = [x.copy() for x in empty]
    for y in range(len(input)):
        for x in range(len(input[0])):
            next[y][x] = str(neighbours(input, x, y))

    return next


def step(input, empty: list[str]):
    next = [x.copy() for x in empty]
    for y in range(len(input)):
        for x in range(len(input[0])):
            next[y][x] = newOccupation(input, x, y)

    return next

def solve(stdscr, input):
    input = [list(x) for x in input]
    draw(stdscr, input, 0)
    stdscr.getkey()

    next = [x.copy() for x in input]
    while True:
        #neig = neighbourTable(next, input)
        #draw(stdscr, neig, '..')
        #stdscr.getkey()

        next = step(next, input)

        counter = sum([x.count('#') for x in next])

        draw(stdscr, next, counter)

        #stdscr.getkey()

if __name__ == "__main__":
    wrapper(main)
