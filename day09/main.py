import sys

caves = []
for i in sys.stdin:
    caves.append(i.strip())

def get_neghbours(i, j):
    n1 = (i-1, j)
    n2 = (i, j+1)
    n3 = (i, j-1)
    n4 = (i+1, j)

    res = []
    if -1 not in n1:
        res.append(n1)
    if len(caves[0]) not in n2:
        res.append(n2)
    if len(caves) not in n4:
        res.append(n4)
    res.append(n3)

    return res

def at(t):
    return int(caves[t[0]][t[1]])

def part1():
    ans = 0
    for i in range(0, len(caves)):
        for j in range(0, len(caves[0])):
            c = 0
            h = int(caves[i][j])
            ns = get_neghbours(i, j)
            for n in ns:
                if at(n) > h:
                    c += 1
            if c == len(ns):
                print(ns, i, j, h)
                ans += h+1

    print(ans)

part1()
