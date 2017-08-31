def young_physicist():
    n_forces = int(input())
    resultant = [0, 0, 0]
    for _ in range(0, n_forces):
        x, y, z = input().split()
        resultant[0] += int(x)
        resultant[1] += int(y)
        resultant[2] += int(z)
    for axe in resultant:
        if axe != 0:
            print ('NO')
            return
    print ('YES')
        
    
                
    
if __name__ == '__main__':
    young_physicist()