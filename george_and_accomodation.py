def george_and_accomodation():
    n_rooms = int(input())
    n_free_rooms = 0
    for _ in range(0, n_rooms):
        occupation, capacity = input().split()
        occupation = int(occupation)
        capacity = int(capacity)
        
        if capacity-occupation >= 2:
            n_free_rooms += 1
    print (n_free_rooms)
    
    
if __name__ == '__main__':
    george_and_accomodation()
        
        
