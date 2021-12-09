import sys
#from sol import parse
from itertools import permutations

o_segments = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
posn = []
for w in o_segments:
    temp = []
    for c in w:
        temp.append(int(ord(c) - ord('a')))
    posn.append(temp)

def solve():
    ans = 0
    d = ['' for i in range(7)]
    A, B = list(map(lambda x : x.split(), line.split('|')))

    for i, a in enumerate(A):
        A[i] = ''.join(sorted(a))

    for i, b in enumerate(B):
        B[i] = ''.join(sorted(b))

    for perm in permutations('abcdefg'):
        ok = True
        for i,c in enumerate(perm):
            d[i] = c

        new = [[d[i] for i in pos] for pos in posn]

        for i, p in enumerate(new):
            new[i]="".join(sorted(p))


        for p in new:
            if p not in A:
                ok = False
            
        if ok:
            print('GOT')
            print(d)
            
            ndig = []
            for dig in B:
                ndig.append(list(map(lambda x: d.index(x), dig)))


            print(ndig)
            res = []
            for dig in ndig:
                res.append("".join([chr(ord('a')+i) for i in dig]))

            for i in range(len(res)):
                res[i] = "".join(sorted(res[i]))

            ans += 1000*o_segments.index((res[0])) + 100*o_segments.index((res[1])) + 10*o_segments.index((res[2])) + o_segments.index((res[3]))

            print(res)
            print(ans)

    return ans
        


ans = 0
for line in sys.stdin:
    ans += solve()

print(ans)



#print(res)




# 1 => 2 segments
# 7 => 3 segments
# 4 => 4 segments
# 8 => 7 segments

# 2, 3, 5 => 5 segments
# 0, 6, 9 => 6 segments


