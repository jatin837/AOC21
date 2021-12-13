with open('input', 'r') as f:
    inp = f.read().split('\n\n')


a, b = inp

ps = []

for line in a.split('\n'):
    x, y = line.split(',')
    ps.append([int(x), int(y)])


ins = b[0]

ins = b.split('\n')[0].split()[2].split('=')
print(ins)
max_x = 2*int(ins[1])

if ins[0] == 'x':
    res = list()
    for i in range(int(max_x//2)):
        current = list(filter(lambda p:p[0]==i, ps))
        to_change = list(map(lambda p: [i, p[1]], list(filter(lambda p:p[0]==max_x-i, ps))))
        print('-'*10)
        print(current)
        print(to_change)
        if len(to_change) != 0:
            for change in to_change:
                if change not in current:
                    res.append(change)
        for curr in current:
            res.append(curr)
        print(len(res))
        print(res)
        print('-'*10)


elif ins[0] == 'y':
    res = list()
    for i in range(int(max_x//2)):
        current = list(filter(lambda p:p[1]==i, ps))
        to_change = list(map(lambda p: [p[0], i], list(filter(lambda p:p[1]==max_x-i, ps))))
        print('-'*10)
        print(current)
        print(to_change)
        print('-'*10)
        if len(to_change) != 0:
            for change in to_change:
                if change not in current:
                    res.append(change)
            for curr in current:
                res.append(curr)
        else:
            continue

print(res)
print(len(res))

