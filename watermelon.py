def watermelon():
    w = int(input())
    for w1 in range(2, w-1, 2):
        if (w-w1) % 2 == 0:
            print ('YES')
            return
    print ('NO')

if __name__ == '__main__':
    watermelon()
    