def way_too_long_words():
    n = int(input())
    for _ in range(0, n):
        word = str(input())
        if len(word) <= 10:
            print(word)
        else:
            print(word[0]+str(len(word)-2)+word[-1])
        

if __name__ == '__main__':
    way_too_long_words()
    