def writerandom():
    import random
    nf = open('numbers.txt.', 'w+')
    n = int(input('number of random='))
    a = 0
    for i in range(n):
        a = random.randint(1, 500)
        nf.write(str(a) + '\n')
writerandom()