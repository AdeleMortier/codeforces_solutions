from collections import Counter

def taxi():
    n_groups = int(input())
    groups = str(input()).split()
    groups = [int(i) for i in groups]
    
    groups = Counter(groups)
    
    n_taxis = groups[4]
    
    n_groups_3 = groups[3]
    n_groups_1 = groups[1]
    n_groups_2 = groups[2]
    
    n_taxis += n_groups_3
    n_groups_1 -= min(n_groups_3, n_groups_1)
    
    n_taxis += n_groups_2//2
    n_groups_2 = n_groups_2 % 2
    
    if n_groups_2 == 1:
        n_taxis += 1
        n_groups_1 -= min(n_groups_1, 2)
        
    n_taxis += n_groups_1//4
    n_groups_1 = n_groups_1 % 4
    
    if n_groups_1 != 0:
        n_taxis += 1
    
    
    print(n_taxis)
    
        
    

if __name__ == '__main__':
    taxi()
    