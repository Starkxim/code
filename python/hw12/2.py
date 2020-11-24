def flcotent():
    num=0
    flname = input('ener filename:')
    with open(flname) as infile:
        for line in infile:
            try:
                num+=1
                print(num,':',line)
            except:
                print('error')
flcotent()