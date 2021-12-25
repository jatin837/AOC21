with open('input', 'r') as f:
    INPUT = f.read()

INPUT = INPUT.strip().split('\n')
INPUT = list(map(list, INPUT))


s = 0
while True:

    s += 1
    c1 = []
    c2 = []
    for i in range(len(INPUT)):
        for j in range(len(INPUT[i])):
            if INPUT[i][j] == '>' and INPUT[i][(j+1)%len(INPUT[i])] == '.':
                c1.append((i, j))

    for c in c1:
        INPUT[c[0]][c[1]] = '.'
        INPUT[c[0]][(c[1]+1)%len(INPUT[0])] = '>'

    for i in range(len(INPUT)):
        for j in range(len(INPUT[i])):
            if INPUT[i][j] == 'v' and INPUT[(i+1)%len(INPUT)][j] == '.':
                c2.append((i, j))

    for c in c2:
        INPUT[c[0]][c[1]] = '.'
        INPUT[(c[0]+1)%len(INPUT)][c[1]] = 'v'
    if len(c1) == len(c2) == 0:
        break

print(s)

