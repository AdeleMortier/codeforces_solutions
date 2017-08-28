def stones_on_the_table():
    n_stones = int(input())
    n_stones_origin = n_stones
    stones = str(input())
    i = 0
    while i < n_stones-1:
        if stones[i] == stones[i+1]:
            n_stones -= 1
            stones = stones[:i+1]+stones[i+2:]
        else:
            i += 1
    print(n_stones_origin - n_stones)
            
    
if __name__ == '__main__':
    stones_on_the_table()