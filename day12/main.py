import sys
from collections import defaultdict

inp = [line.strip().split('-') for line in sys.stdin]

ans = 0

G = defaultdict(list)

for start, end in inp:
    G[start].append(end)
    G[end].append(start)


def count(node, visited=[]):
    global ans
    visited.append(node)

    if node == 'end':
        ans += 1

    else:
        for n in G[node]:
            if n not in visited:
                count(n, visited)
            else:
                continue

    visited.remove(node)

for i in G['start']:
    count(i)

print(ans)
print(G)
print(len(G))
