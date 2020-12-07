import re

with open('input.txt') as f:
    data = [line.rstrip('\n') for line in f]

rootPattern = re.compile(
    r'(\w+ \w+) bags contain (.*)\.'
)

containPattern = re.compile(
    r'(\d+) (\w+ \w+) bag'
)


def parseLine(input: str) -> tuple[str, list[tuple[int, str]]]:
    root = rootPattern.match(input).groups()
    contains = containPattern.findall(root[1])
    contains = [(int(c[0]), c[1]) for c in contains]

    return (root[0], contains)


def solve(input):
    data = [parseLine(i) for i in input]

    todo = ['shiny gold']
    outer = []

    while len(todo) > 0:
        cur = todo.pop()
        for d in data:
            for inner in d[1]:
                if inner[1] == cur and d[0] not in outer:
                    outer.append(d[0])
                    todo.append(d[0])

    #outer.sort()
    return len(outer)

if __name__ == "__main__":
    print(solve(data))
