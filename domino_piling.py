def domino_piling():
    mn = str(input())
    i = mn.find(' ')
    m = int(mn[:i])
    n = int(mn[i+1:])
    if m % 2 == 0 and n % 2 == 0:
        print(int(m*n/2))
        return
    if m % 2 != 0 and n % 2 != 0:
        print (int(m*(n-1)/2 + (m-1)/2))
        return
    print (int(m*n/2))
    
            
    

if __name__ == '__main__':
    domino_piling()
    