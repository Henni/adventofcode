from functools import reduce
from operator import __add__, or_
import pyparsing as pp
from typing import Any

def readData():
    with open('input.txt') as f:
        data = f.read()
    
    # parse
    rules, msgs = data.split('\n\n')
    rules = rules.split('\n')
    rules = dict([r.split(': ') for r in rules])

    return rules, msgs.split('\n')


def grammarGrammar(rule) -> dict[str,dict[Any]]:
    xChar = pp.quotedString.setResultsName('char')
    xNum = pp.Word(pp.nums)
    xExp = pp.Group(xNum('lRule') + xNum('rRule'))
    xRule = pp.Group((xExp('lExp') + '|' + xExp('rExp')) | xChar)('rule')

    return xRule.parseString(rule).asDict()

def translateRule(rules, idx, done):
    if idx in done:
        return

    if rules[idx][0][0].startswith('"'):
        rules[idx] = pp.Char(rules[idx][1])
    else:
        rule = [x.split(' ') for x in rules[idx].split('|')]
        rule = [[x.strip() for x in r] for r in rule]
        rule = [[x for x in r if x] for r in rule]

        [translateRule(rules, x, done) for r in rule for x in r]

        rule = [reduce(__add__, [rules[x] for x in r]) for r in rule]
        rules[idx] = reduce(or_, rule)

    done.append(idx)


def solve():
    rules, msgs = readData()
    translateRule(rules, '0', [])
    valid = 0
    for m in msgs:
        try:
            rules['0'].parseString(m, parseAll=True)
            print('✓ ', m)
            valid += 1
        except:
            print('✗ ', m)
    return valid


if __name__ == "__main__":
    print(solve())
