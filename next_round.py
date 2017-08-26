def next_round():
    nk = str(input()).split()
    n = int(nk[0])
    k = int(nk[1])
    
    contestants = (str(input())).split()
    scores = [int(i) for i in contestants]
    
    k_score = scores[k-1]
    i = 0
    for score in scores[:k]:
        if score <= 0:
            break
        i += 1
    for score in scores[k:]:
        if score < k_score or score <= 0:
            break
        i += 1
    print (i)

            
    

if __name__ == '__main__':
    next_round()
    