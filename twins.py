def twins():
    n_coins = int(input())
    coins = str(input()).split()
    coins = sorted([int(i) for i in coins], reverse=True)
    
    total_sum = sum(coins)
    my_sum = 0
    my_coins = 0
    while my_sum <= total_sum/2:
        my_sum += coins[my_coins]
        my_coins += 1
    print(my_coins)
    
    
if __name__ == '__main__':
    twins()
        
    
   
    
    