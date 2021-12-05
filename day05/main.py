import sys
from collections import Counter

inp = sys.stdin

fq = Counter()

for line in inp:
    start, end = line.split('->')
    x1, y1 = tuple(map(int,start.split(',')))
    x2, y2 = tuple(map(int,end.split(',')))


    if x1 == x2:
        a = min(y1, y2)
        b = max(y1, y2)
        for i in range(a, b+1):
            fq[(x1, i)] += 1

    if y1 == y2:
        a = min(x1, x2)
        b = max(x1, x2)
        for i in range(a, b+1):
            fq[(i, y1)] += 1

    if x2-x1 == y2-y1:
        a = min(x1, x2)
        b = max(x1, x2)
        c = min(y1, y2)
        d = max(y1, y2)

        for i in range(b - a + 1):
            fq[(a+i, c+i)] += 1

    if x2-x1 == -(y2-y1):
        a = min(x1, x2)
        b = max(x1, x2)
        c = min(y1, y2)
        d = max(y1, y2)

        for i in range(b - a + 1):
            fq[(a+i, d-i)] += 1


ans = 0

for k in list(fq.keys()):
    if fq[k] >= 2:
        ans +=1 


print(ans)
#print(fq)
