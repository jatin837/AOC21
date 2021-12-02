def read_input(iname = 'input'):
    with open(iname, 'r') as f:
        inp = f.readlines()
        direction = []
        value = []
        for i in inp:
            direction.append(i.split()[0])
            value.append(int(i.split()[1]))
    return direction, value 

def main():
    directions, values = read_input('testinput')
    L = len(values)

    l = 0
    w = 0

    for i in range(L):
        direction = directions[i]
        value = values[i]

        if direction == 'up':
            l -= value
        if direction == 'down':
            l += value
        if direction == 'forward':
            w += value

    print(l*w)

def main2():
    directions, values = read_input('input')

    L = len(values)
    aim = 0

    w = 0
    l = 0
    d = 0

    inc_dep = 0

    for i in range(L):
        direction = directions[i]
        value = values[i]

        if direction == 'up':
            l -= value
            aim = l
        if direction == 'down':
            l += value
            aim = l
        if direction == 'forward':
            w += value
            d += aim*value

    print(l)
    print(w)
    print(d)
    print(l*w)
    print(w*d)

