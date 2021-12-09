import sys

caves = [] 
for i in sys.stdin:
    caves.append([int(c) for c in i.strip()])

def isvalid(p):
    if p[0] >=0 and p[0] < len(caves) and p[1] >= 0 and p[1] < len(caves[0]):
        return True
    return False

def get_neghbours(i, j):
    n1 = (i-1, j)
    n2 = (i, j+1)
    n3 = (i, j-1) 
    n4 = (i+1, j)

    res = []
    for n in [n1, n2, n3, n4]:
        if isvalid(n):
            res.append(n)

    return res


def part1():
    ans = 0
    res = []
    for i in range(0, len(caves)):
        for j in range(0, len(caves[0])):
            c = 0
            h = int(caves[i][j])
            ns = get_neghbours(i, j)
            for n in ns:
                if caves[n[0]][n[1]] > h:
                    c += 1
            if c == len(ns):
                ans += h+1
                res.append((i, j))

    print('ans1 = ', ans)
    return res

lps = part1()
print(lps)


def part2():
    ans = []
    print('lps', lps)
    for lp in lps:
        print('lp', lp)
        c = 0
        stack = [lp]
        visited = set(lp)
        while len(stack) != 0:
            p = stack[-1]
            print('p',p)
            nbs = get_neghbours(*p)
            stack.pop()
            for nb in nbs:
                if nb not in visited and caves[nb[0]][nb[1]] != 9:
                    c += 1
                    stack.append(nb)
                    visited.add(nb)

        ans.append(c)

    ans.sort()
    ans.reverse()
    print(c)
    print(ans[0]*ans[1]*ans[2]))

part2()
