def readrandom():
    total = 0
    howmany = 0
    with open('numbers.txt') as infile:
        for line in infile:
            try:
                num = int(line)
                total += num
                howmany += 1
                print(num)
            except IOError as ercode:
                print("Error:",str(ercode))
            except ValueError:
                print('Error:this is not a number')

    print(total, howmany)
readrandom()