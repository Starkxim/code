def sum():
    total = 0
    with open('numbers.txt') as infile:
        for line in infile:
            try:
                num = int(line)
                total += num
            except ValueError:
                print('error')

    print(total)
sum()