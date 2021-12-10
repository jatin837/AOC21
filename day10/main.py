import sys
from collections import Counter, deque

d = {
    "[" : "]",
    "<" : ">",
    "{" : "}",
    "(" : ")",
}

val = {
    ']' : 57,
    '>' : 25137,
    ')' : 3,
    '}' : 1197,
    '' : 0,
}

ans = 0
for line in sys.stdin:
    stack = []
    ill = ''
    for ch in line.strip():
        if ch in d.keys():
            stack.append(ch)
        if ch in d.values() and ch != d[stack[-1]]:
            ill = ch
            break
        if ch in d.values() and ch == d[stack[-1]]:
            stack.pop()
            
    ans += val[ill]

print(ans)

