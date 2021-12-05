import sys

inp = sys.stdin

for line in inp:
    start, end = line.split('->')
    x1, y1 = tuple(map(int,start.split(',')))
    x2, y2 = tuple(map(int,end.split(',')))
    print(x1, y1, x2, y2)
