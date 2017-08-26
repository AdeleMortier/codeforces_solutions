def next_round():
    nk = str(input())
    space = nk.index(' ')
    n = int(nk[:space])
    k = int(nk[space+1:])    
    contestants = str(input())
    scores = []
    space = contestants.find(' ')
    if space == -1:
        scores.append(int(contestants))
    else:
        scores.append(int(contestants[:space]))
        prev_space = space
        flag = 0
        while True:
            space = contestants.find(' ', prev_space+1)
            if space == -1:
                flag = 1
                score = contestants[prev_space:]
            else:
                score = contestants[prev_space:space]
            scores.append(int(score))
            if flag == 1:
                break
            prev_space = space
            
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
    