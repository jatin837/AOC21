import sys
from collections import Counter, deque


inp = [[int(n) for n in line.strip()] for line in sys.stdin]

N = len(inp)
M = len(inp[0])

dr = [1, -1, 1, -1, 0, 0, 1, -1]
dc = [-1, +1, 1, -1, 1, -1, 0, 0]

print('initial')
for l in inp:
    print(l)

ans = 0
for step in range(2):
    print('step', step+1)
    for r in range(N):
        for c in range(M):
            if inp[r][c] < 9:
                inp[r][c] += 1
            else:
                q = deque()
                q.append((r, c))
                visited = [(r,c)]
                while q:
                    rq, cq = q.popleft()
                    print('visit', rq, cq)
                    inp[rq][cq] += 1
                    for i in range(8):
                        rr = rq + dr[i]
                        cc = cq + dc[i]
                        if rr >= 0 and rr < N and cc >=0 and cc < M and inp[rr][cc]>9:
                            print('now visit', rr, cc)
                            inp[rr][cc] += 1
                            if (rr, cc) not in visited:
                                q.append((rr, cc))
                                visited.append((rr, cc))
                      #     if inp[rr][cc] > 9 and (rr, cc) not in visited:
                      #         q.append((rr, cc))
                      #         visited.append((rr, cc))
                      #     else:
                      #         continue
                      # else:
                      #     continue

for l in inp:
    print(l)
            




