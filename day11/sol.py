import sys
from collections import deque

inp = [[int(c) for c in line] for line in sys.stdin]

R = len(inp)
C = len(inp[0])

q = deque()
for r in range(R):
    for c in range(C):
        if 0<inp[r][c]<9:
            inp[r][c] += 1

        if inp[r][c] == 0:
            deque.append((r, c))

