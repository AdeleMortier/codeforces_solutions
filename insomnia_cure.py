def insomnia_cure():
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    d = int(input())
    
    damages = [k, l, m, n]
    damaged = 0
    for i in range(1, d+1):
        for number in damages:
            if i % number == 0:
                damaged += 1
                break
    print (damaged)
    
    
if __name__ =='__main__':
    insomnia_cure()