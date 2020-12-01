input = [138307, 654504]

counter = 0

def mono(x):
    prev = 0
    for s in str(x):
        if int(s) < prev:
            return False
        prev = int(s)
    return True

def adj(x):
    count = 0
    prev = None
    for s in str(x):
        if s == prev:
            count += 1
        else:
            if count == 2:
                return True
            count = 1
        prev = s

    return count == 2

for x in range(input[0], input[1] + 1):
    if mono(x) and adj(x):
        counter += 1

print(counter)