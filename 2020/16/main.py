import math

def readData():
    with open('input.txt') as f:
        data = f.read()
    
    # parse
    (fields, my, other) = data.split('\n\n')

    fields = fields.split('\n')
    my = my.split('\n')[1]
    my = [int(x) for x in my.split(',')]
    other =  other.split('\n')[1:]
    other = [[int(x) for x in t.split(',')] for t in other]

    fields = parseFields(fields)

    return fields, my, other

def parseFields(data):
    newData = []
    for d in data:
        (title, sRanges) = d.split(': ')
        ranges = [[int(x) for x in r.split('-')] for r in sRanges.split(' or ')]

        newData.append((title, ranges))

    return dict(newData)

def isMatch(value, ranges):
    for r in ranges:  # ranges
        if r[0] <= int(value) <= r[1]:
            return True
    return False

def isValidField(field, fields):
    for f in fields:
        for r in f:  # ranges
            if r[0] <= field <= r[1]:
                return True
    return False

def isValidTicket(ticket, fields):
    return all(isValidField(x, fields) for x in ticket)

def errorRate(ticket, fields):
    return sum(x for x in ticket if not isValidField(x, fields))

def solve():
    fields, my, other = readData()

    other = [x for x in other if isValidTicket(x, fields.values())]

    print(len(other))

    values = []
    for idx in range(len(other[0])):
        values.append(fields.keys())
        for t in other:
            values[-1] = [k for k in fields.keys() if k in values[-1] and isMatch(t[idx], fields[k])]

    modified = True
    uniques = set()
    while modified:
        modified = False
        for i, v in enumerate(values):
            if len(v) == 1 and v[0] not in uniques:
                uniques.add(v[0])
                modified = True
            elif len(v) > 1 and any(u in v for u in uniques):
                modified = True
                values[i] = [x for x in v if x not in uniques]

    if all(len(x)==1 for x in values):
        print('Found structure')
    structure = [x[0] for x in values]

    departureIdxs = [i for i,x in enumerate(structure) if x.startswith('departure')]

    return math.prod([my[i] for i in departureIdxs]) 

if __name__ == "__main__":
    print(solve())
