import sys
from collections import Counter, deque


inp = [[int(n) for n in line.strip()] for line in sys.stdin]

N = len(inp)
M = len(inp[0])

dr = [1, -1, 1, -1, 0, 0, 1, -1]
dc = [-1, +1, 1, -1, 1, -1, 0, 0]

#########
#       #
# 11111 #
# 19991 #
# 19191 #
# 19991 #
# 11111 #
#       #
#########
ans = 0
nz = 0
count = 0
while nz != N*M:
    nz = 0
    count += 1
    q = deque()
    for r in range(N):
        for c in range(M):
            if inp[r][c]+1 != 10:
                inp[r][c] += 1
            else:
                q.append((r, c))

    while q:
        ans += 1
        rq, cq = q.popleft()
        inp[rq][cq] = 0
        nz += 1
        for i in range(8):
            rr = rq + dr[i]
            cc = cq + dc[i]
            if 0<=rr<N and 0<=cc<M and inp[rr][cc] != 0:
                inp[rr][cc] += 1
                if inp[rr][cc] == 10 and (rr, cc) not in q:
                    q.append((rr, cc))
    print('count',count)
    print('nz',nz)
    for l in inp:
        print(l)
                            
print(count)

print(ans)
