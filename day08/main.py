import sys
from sol import parse

pattern, output = list(), list()

res1 = 0
res2 = 0
for line in sys.stdin:
    A, B = list(map(lambda x : x.split(), line.split('|')))
    pattern.append(A)
    output.append(B)
    n = parse_pattern(A)

    p = parse(A)

    for o in B:
        if len(o) in [2, 3, 4, 7]:
            res1 += 1


def parse_pattern(A):
    A.sort(key=len)
    out = [-1 for i in range(10)] 
    out[1] = A[0]
    out[7] = A[1]
    out[4] = A[2]
    out[8] = A[9]

    cf = A[0]
    a = ''
    for c in A[1]:
        if c not in A[0]:
            a = c
            break

    bd = ''
    for c in A[2]:
        if c not in A[1]:
            bd += c


    eg = ''
    for c in A[9]:
        if c not in set(A[1] + A[9])
        eg += c
    

    for i in A[6:9]:
        if (eg[0] or eg[1]) not in i:
            out[6] = i
            break

    for i in A[6:9]:
        if (cf[0] or cf[1]) not in i:
            out[9] = i
            break






assert len(pattern) == len(output)
assert len(pattern[0]) == 10
assert len(output[0]) == 4

# 1 => 2 segments
# 7 => 3 segments
# 4 => 4 segments
# 8 => 7 segments

# 2, 3, 5 => 5 segments
# 0, 6, 9 => 6 segments


o_segments = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]

print(pattern, output)
print(res1)
