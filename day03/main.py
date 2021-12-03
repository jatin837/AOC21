import numpy as np

def read_input(path='input'):
    with open(path , 'r') as f:
        inp = list(map(lambda x : x.strip(), f.readlines()))
    return inp


def main():
    reports = read_input('input')
    L = len(reports[0])

    n_one = np.zeros(L)
    n_zero = np.zeros(L)

#    breakpoint()

    for report in reports:
        for i in range(L):
            if report[i] == '0':
                n_zero[i] += 1
            else:
                n_one[i] += 1

#    breakpoint()

    mcb = ''
    lcb = ''
    for i in range(L):
        if n_one[i] >= n_zero[i]:
            mcb += '1'
            lcb += '0'
        else:
            mcb += '0'
            lcb += '1'

    gamma = int(mcb, 2)
    epsilon = int(lcb, 2)

#    breakpoint()

    return (mcb, lcb, reports)



def main2():
    _, _, reports = main()

    ox_gen = reports.copy()
    co_scr = reports.copy()
    
    L = len(ox_gen[0])

    for i in range(L):
        if len(ox_gen) == 1:
            break
        ox_gen = remove_unwanted(ox_gen, i, t = 'ox')

    for j in range(L):
        if len(co_scr) == 1:
            break
        co_scr = remove_unwanted(co_scr, j, t = 'co')

    co_scr = int(co_scr[0], 2)
    ox_gen = int(ox_gen[0], 2)
    print(co_scr, ox_gen)
    print(co_scr*ox_gen)
    breakpoint()

def remove_unwanted(initial_list, position, t):
    n0 = n1 = 0

    for record in initial_list:
        if record[position] == '0':
            n0 += 1
        else:
            n1 += 1

    out = []

    if t == 'co':
        if n0 <= n1:
            out_num = '0'
        else:
            out_num = '1'
    elif t == 'ox':
        if n1 >= n0:
            out_num = '1'
        else:
            out_num = '0'

    for rec in initial_list:
        if rec[position] == out_num:
            out.append(rec)

    return out
            

# initial list, position_num --> output_list
