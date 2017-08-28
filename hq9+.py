def hq9plus():
    prog = str(input())
    instructions = ['H', 'Q', '9']
    for char in prog:
        if char in instructions:
            print('YES')
            return
    print ('NO')
    
if __name__ == '__main__':
    hq9plus()
        