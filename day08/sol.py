def parse(p):
    p.sort(key=len)
    cf = p[0]
    bd = ''
    for c in p[2]:
        if c not in p[1]:
            bd += c

    eg = ''
    for c in p[-1]:
        if c not in set(p[2] + p[1]):
            eg += c

    res = [-1 for i in range(10)]
    res[8] = p[-1]
    res[1] = cf
    res[4] = p[2]
    res[7] = p[1]

    for i in p[6:9]:
        if (eg[0] or eg[1]) not i:
            res[9] = i
            break

    for i in p[6:9]:
        if (bd[0] or bd[1]) not i:
            res[0] = i
            break

    for i in p[6:9]:
        if (cf[0] or cf[1]) not i:
            res[6] = i
            break

    for i in p[3:6]:
        for c in i:
            if c not in res[9]:
                res[2] = i
                break

    for i in p[3:6]:
        if (cf[0] and cf[1]) in i:
            res[3] = i

    for i in p[3:6]:
        if (eg[0] or eg[1]) not in i and res[i] == -1:
            res[5] = i

    return res




