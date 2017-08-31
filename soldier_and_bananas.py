def soldier_and_bananas():
    k, n, w = input().split()
    k = int(k)
    n = int(n)
    w = int(w)
    
    price = sum([i*k for i in range(1, w+1)])
    print (max(0, price-n))

    
    
if __name__ == '__main__':
    soldier_and_bananas()