from copy import copy
from collections import Counter

with open('input', 'r') as f:
    inp = f.read()


init_seq, rules = inp.strip().split('\n\n')

rule = {}

for r in rules.split('\n'):
    a, b = r.strip().split('->')
    rule[a.strip()] = b.strip()


C1 = Counter()

for i,ch in enumerate(init_seq[:-1]):
    d = ch + init_seq[i+1]
    C1[d] += 1
 

for _ in range(40):
    C2 = Counter()
    for k, v in C1.items():
        if k in rule.keys():
            C2[k[0] + rule[k]] += v 
            C2[rule[k] + k[1]] += v
        else:
            C2[k] += v

    C1 = C2

C3 = Counter()
for k, v in C1.items():
    C3[k[0]] += 1*v
    C3[k[1]] += 1*v

a = max(C3.values())
b = min(C3.values())
print(a-b)
print((a-b)//2)


# ABC -> AM, MB, BD, DC
