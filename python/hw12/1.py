def fifth():
    num = 0
    flname = input('ener filename:')
    with open(flname) as infile:
        for line in infile:
            try:
                if num < 5:
                    print(line)
                    num += 1
            except:
                print('error')
fifth()