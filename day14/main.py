from copy import copy
from collections import Counter

with open('input', 'r') as f:
    inp = f.read()


init_seq, rules = inp.strip().split('\n\n')

rule = {}
for r in rules.split('\n'):
    a, b = r.strip().split('->')
    rule[a.strip()] = b.strip()


for s in range(40):
    print(s)
    new_seq = ''
    for i,ch in enumerate(init_seq[:-1]):
        d = ch + init_seq[i+1]
        if d in rule.keys():
            new_seq += ch + rule[d]
        else:
            new_seq += ch
    new_seq += init_seq[-1]
    init_seq = new_seq
    print(init_seq)


counter = Counter()
for c in init_seq:
    counter[c] += 1

print(max(counter.values()) - min(counter.values()))
