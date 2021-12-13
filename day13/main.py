from copy import copy
with open('input', 'r') as f:
    inp = f.read().split('\n\n')


a, b = inp

ps = []

for line in a.split('\n'):
    x, y = line.split(',')
    ps.append([int(x), int(y)])



inss = b.strip().split('\n')

for ins in inss:
    d, v = ins.strip().split()[-1].split('=')
    v = int(v)

    if d == 'x':
        w = v
        res = list()
        for i in range(int(v)):
            current = list(filter(lambda p:p[0]==i, ps))
            to_change = list(map(lambda p: [i, p[1]], list(filter(lambda p:p[0]==2*v-i, ps))))
            for curr in current:
                res.append(curr)
            if len(to_change) != 0:
                for change in to_change:
                    if change not in current:
                        res.append(change)
            else:
                continue


    elif d == 'y':
        l = v
        res = list()
        for i in range(int(v)):
            current = list(filter(lambda p:p[1]==i, ps))
            to_change = list(map(lambda p: [p[0], i], list(filter(lambda p:p[1]==2*v-i, ps))))
            for curr in current:
                res.append(curr)
            if len(to_change) != 0:
                for change in to_change:
                    if change not in current:
                        res.append(change)
            else:
                continue
    ps = res.copy()



ans = ''
for i in range(l):
    for j in range(w):
        if [j, i] in ps:
            ans += 'X'
        else:
            ans += ' '

    ans += '\n'

print(ans)
