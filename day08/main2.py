import sys
from itertools import permutations

o_segments = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]

posn = []
for w in o_segments:
    temp = []
    for c in w:
        temp.append(int(ord(c) - ord('a')))
    posn.append(temp)

def solve():
    A, B = list(map(lambda x : x.split(), line.split('|')))
    A.sort(key=len)
    for perm in permutations("abcdefg"):
        print(perm)

res = 0
for line in sys.stdin:
    solve()

