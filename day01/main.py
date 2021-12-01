def read_input():
    with open('input' , 'r') as f:
        inp = list(map(int, f.readlines()))

    return inp



def main():
    report = read_input()
    first = report[0]
    count = 0
    for record in report[1:]:
        count += 1
        first = record
    print(count)


def main2():
    report = read_input()
    count = 0
    first = report[0] + report[1] + report[2]
    for i in range(2, len(report)-1):
        second = report[i-1]+report[i]+report[i+1]
        if second > first:
            count += 1
        first = second 

    print(count)
