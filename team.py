def team():
    n = int(input())
    res = 0
    for _ in range(0, n):
        trio = str(input())
        p = int(trio[0])
        v = int(trio[2])
        t = int(trio[4])
        agree = p+v+t
        if agree >= 2:
            res += 1
    print (res)
            
    
            
    

if __name__ == '__main__':
    team()
    