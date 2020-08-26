with open('sums.txt', 'rt') as file:  # read sums.txt
    for line in file:
        print(sum(int(number) for number in line.split()))
