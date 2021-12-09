for lp in lps:
    c = 0
    stack = [lp]
    visited = set(lp)
    while len(stack) != 0:
        stack.pop()
        nbs = get_neghbours(*lp)
        for nb in nbs:
            if nb not in visited and caves[nb[0]][nb[1]] != 9:
                c += 1
                stack.append(nbs)
                visited.add(nb)

    print(c)
