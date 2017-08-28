def beautiful_matrix():
    found = 0
    n_row = 0
    while n_row <= 4:
        row = str(input()).split()
        row = [int(i) for i in row]
        if 1 in row:
            n_col = row.index(1)
            n_manip_col = abs(2-n_col)
            n_manip_row = abs(2-n_row)
            print(n_manip_row+n_manip_col)
            return
        n_row += 1
        
    
    
if __name__ == '__main__':
    beautiful_matrix()
    