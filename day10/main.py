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

val2= {
    ']' : 2,
    '>' : 4,
    ')' : 1,
    '}' : 3,
}
ans = 0
scores = []
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
            
    if ill == '':
        stack.reverse()
        score = 0
        for ch in stack:
            score = 5*score + val2[d[ch]]
        scores.append(score)




    ans += val[ill]


scores.sort()
print(scores[len(scores)//2])
