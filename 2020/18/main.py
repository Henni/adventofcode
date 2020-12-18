import pyparsing as pp

def readData():
    with open('input.txt') as f:
        data = f.read()
    
    # parse
    data = data.split('\n')

    return data


def parseExpression(input):
    xNum = pp.Word(pp.nums)
    xOp  = pp.Char('+') | pp.Char('*')
    exp  = xOp | xNum
    nest = pp.nestedExpr('(', ')', content=exp,)
    
    return nest.parseString(input).asList()


def calcExpression(exp):
    # recurse
    for i,x in enumerate(exp):
        if type(x) is list:
            exp[i] = calcExpression(x)

    print(exp)
    
    # addition
    for i,x in enumerate(exp):
        if x == '+':
            exp[i+1] = int(exp[i-1]) + int(exp[i+1])
            exp[i-1] = None
            exp[i]   = None
        elif x == '*':
            exp[i+1] = int(exp[i-1]) * int(exp[i+1])
            exp[i-1] = None
            exp[i] = None

    # clean
    exp = [x for x in exp if x != None]

    return exp[0]


def solve():
    data = readData()
    data = [d.replace(' ','') for d in data]
    res = 0
    for d in data:
        exp = parseExpression('('+d+')')[0]
        res += calcExpression(exp)

    return res


if __name__ == "__main__":
    print(solve())
