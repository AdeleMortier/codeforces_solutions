def theatre_square():
    nma = str(input())
    space1 = nma.index(' ')
    n = int(nma[:space1])
    space2 = nma.index(' ', space1+1)
    m = int(nma[space1+1:space2])
    a = int(nma[space2+1:])
    if a > n:
        number_n = 1
    elif n/a == int(n/a):
        number_n = int(n/a)
    else:
        number_n = int(n/a)+1
    if a > m:
        number_m = 1
    elif m/a == int(m/a):
        number_m = int(m/a)
    else:
        number_m = int(m/a)+1

    print (number_n*number_m)
    

if __name__ == '__main__':
    theatre_square()
    