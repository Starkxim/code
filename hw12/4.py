def arithmetic():
    total = 0
    howmany = 0
    with open('numbers.txt') as infile:
        for line in infile:
            try:
                num = int(line)
                total += num
                howmany += 1
            except ValueError:
                print('error')

    print(total/howmany)
arithmetic()