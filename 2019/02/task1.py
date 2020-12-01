import sys

with open('input.txt') as f:
    data = f.readlines()

data = data[0].split(',')
data = [int(d) for d in data]
orig = data

goal = 19690720

for noun in range(100):
    for verb in range(100):
        data = list(orig)
        data[1] = noun
        data[2] = verb
        i = 0

        while True:
            opcode = data[i]
            
            if opcode == 99:
                break

            if opcode == 1:
                data[data[i+3]] = data[data[i+1]] + data[data[i+2]]

            if opcode == 2:
                data[data[i+3]] = data[data[i+1]] * data[data[i+2]]

            i += 4

        print(data[0], end=' ')
        if data[0] == goal:
            print(noun, verb)
            print(100*noun+verb)
            sys.exit(0)

print('fin')
