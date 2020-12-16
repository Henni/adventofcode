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

    return newData

def isValidField(field, fields):
    for f in fields:
        for r in f[1]: # ranges
            if r[0] <= field <= r[1]:
                return True
    return False

def errorRate(ticket, fields):
    return sum(x for x in ticket if not isValidField(x, fields))

def solve():
    fields, _, other = readData()

    return sum(errorRate(t, fields) for t in other)

if __name__ == "__main__":
    print(solve())
