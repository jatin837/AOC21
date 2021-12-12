import sys
from collections import defaultdict

inp = [line.strip().split('-') for line in sys.stdin]

ans = 0

G = defaultdict(list)

for start, end in inp:
    G[start].append(end)
    G[end].append(start)


#   visited = []
#   def count(node):
#       global ans
#       global visited
#       
#       if node == 'end':
#           ans += 1

#       else:
#           for n in G[node]:
#               if n not in visited:
#                   print(node + n)
#                   visited.append(n)
#                   count(n)

#   for i in G['start']:
#   count(i)

print(G)
print(len(G))
