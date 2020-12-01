import math

with open('input.txt') as f:
    data = f.readlines()

data = [d[:-1] for d in data]

def calc_fuel(mass):
    fuel = math.floor(mass / 3 - 2)

    if fuel <= 0:
        return 0

    return fuel + calc_fuel(fuel)

data = [calc_fuel(int(d)) for d in data]

print(sum(data))
# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.
