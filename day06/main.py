istate = list(map(int, input().split(',')))
from collections import Counter
#istate = [3, 4, 3, 1, 2]

def solve(i):

    out = istate.copy()
    c = Counter()

    for state in istate:
        c[state] += 1

    for day in range(1, i+1):
        y = Counter()
        for k, v in c.items():
            if k == 0:
                y[6] += v
                y[8] += v
            else:
                y[k-1] += v

        c = y

    return c

####for i in range(1, i+1):
####    print('day', i)
####    print(len(out))
####    for j in range(len(out)):
####        if out[j] == 0:
####            out[j] = 6
####            out.append(8)
####        else:
####            out[j] -= 1
####    
####return out

print(solve(1))
print('-'*10)
print(solve(2))

ans = 0
for _, v in solve(256).items():
    ans += v

print('ans', ans)
#print(256, len(solve(256)))
