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


def is_bingo(m_board):
    r_sum = 0
    for rn in range(5):
        for cn in range(5):
            r_sum += m_board[5*rn + cn]
        if r_sum == 5:
            return True
        else:
            r_sum = 0
    c_sum = 0
    for cn in range(5):
        for rn in range(5):
            c_sum += m_board[5*rn + cn]
        if c_sum == 5:
            return True
        else:
            c_sum = 0

    return False


    

def main():
    inp = read_input()
    orders = inp['order']
    boards = inp['boards']
    m_board = [[0 for i in range(25)] for j in range(len(boards))]

    for num in orders:
        for i, board in enumerate(boards):
            if num in board:
               m_board[i][board.index(num)] = 1
            if is_bingo(m_board[i]):
                print(f"{i}-yes")
            else:
                print('no')
