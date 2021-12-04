from collections import Counter

def read_input():
    with open('input' , 'r') as f:
        inp = f.read()
    breakpoint()
    out = parse(inp)

    return out

def parse(inp):
    out = Counter()
    inp = inp.split('\n\n')

    out['order'] = list(map(int, inp[0].split(',')))
    out['boards'] = [list(map(int, inp[i].split())) for i in range(1, len(inp))]


    return out


    

def main():
    inp = read_input()
    orders = inp['order']
    boards = inp['boards']
