def tram():
    n_stations = int(input())
    max_capa = -1
    capa = 0
    for _ in range(0, n_stations):
        [exit, enter] = str(input()).split()
        exit = int(exit)
        enter = int(enter)
        capa = capa - exit + enter
        if capa > max_capa:
            max_capa = capa
    print(max_capa)
    
    
if __name__ == '__main__':
    tram()
    