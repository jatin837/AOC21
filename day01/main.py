def read_input():
    with open('input' , 'r') as f:
        inp = list(map(int, f.readlines()))

    return inp



def main():
    report = read_input()
    first = report[0]
    count = 0
    for record in report[1:]:
        if record > first:
            print('yes')
            count += 1
        else:
            print('no')
        first = record

    print(count)


