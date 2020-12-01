import sys

with open('input.txt') as f:
    data = f.readlines()

#data = ['3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99']

data = data[0].split(',')
data = [int(d) for d in data]

# instruction counter
i = 0

def translateParameters(params, modes):
    # ABCDE
    #  1002
    # DE - two-digit opcode,      02 == opcode 2
    #  C - mode of 1st parameter,  0 == position mode
    #  B - mode of 2nd parameter,  1 == immediate mode
    #  A - mode of 3rd parameter,  0 == position mode, omitted due to being a leading zero

    # pad right modes
    modes = modes + (len(params) - len(modes)) * [0]

    return [data[p] if m == 0 else p for p, m in zip(params, modes)]

def step():
    global i
    opcode = data[i] % 100
    modeString = str(data[i])[:-2]
    modes = [int(m) for m in modeString]
    modes.reverse()

    #print(i, opcode, modes, data[i:i+4])

    if opcode == 99: # exit
        pass

    elif opcode == 1: # add
        # ignore 3rd mode
        params = translateParameters(data[i+1:i+3], modes)
        data[data[i+3]] = params[0] + params[1]
        i+=4

    elif opcode == 2: # multiply
        params = translateParameters(data[i+1:i+3], modes)
        data[data[i+3]] = params[0] * params[1]
        i+=4

    elif opcode == 3: # input
        data[data[i+1]] = int(input(f'Instruction #{i}: '))
        i+=2
    
    elif opcode == 4: # output
        params = translateParameters([data[i+1]], modes)
        print(f'Instruction #{i}: {params[0]}')
        i+=2

    elif opcode == 5: # jump non zero
        params = translateParameters(data[i+1:i+3], modes)
        if params[0] != 0:
            i = params[1]
        else:
            i+=3

    elif opcode == 6:  # jump zero
        params = translateParameters(data[i+1:i+3], modes)
        if params[0] == 0:
            i = params[1]
        else:
            i+=3

    elif opcode == 7:  # <
        params = translateParameters(data[i+1:i+3], modes)
        data[data[i+3]] = int(params[0] < params[1])
        i+=4

    elif opcode == 8:  # ==
        params = translateParameters(data[i+1:i+3], modes)
        data[data[i+3]] = int(params[0] == params[1])
        i+=4

    else:
        sys.exit(1)

    return opcode

while True:
    if step() == 99:
        break

print('fin')
