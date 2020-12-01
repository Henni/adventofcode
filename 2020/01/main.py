import math

with open('input.txt') as f:
    data = f.readlines()

data = [int(d[:-1]) for d in data]

def solve(input):
    for i, x in enumerate(input):
        for j, y in enumerate(input[i:]):
            for z in input[j:]:
                if x + y + z == 2020:
                    return x*y*z

print(solve(data))

# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.
