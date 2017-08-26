def bit_plus_plus():
    n_statements = int(input())
    x = 0
    for _ in range(0, n_statements):
        statement = str(input())
        if '+' in statement:
            x += 1
        if '-' in statement:
            x -= 1
    print(x)
    
            
    

if __name__ == '__main__':
    bit_plus_plus()
    