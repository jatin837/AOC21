istate = list(map(int, input().split(',')))
#istate = [3, 4, 3, 1, 2]

def solve(i):
    out = istate.copy()
    for i in range(1, i+1):
        print('day', i)
        for j in range(len(out)):
            if out[j] == 0:
                out[j] = 6
                out.append(8)
            else:
                out[j] -= 1
        
    return out


print(256, len(solve(256)))
