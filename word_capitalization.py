def word_capitalization():
    low_to_up = {'a':'A', 'b':'B', 'c':'C', 'd':'D', 'e':'E', 'f':'F', 'g':'G', 'h':'H', 'i':'I', 'j':'J', 'k':'K', 'l':'L', 'm':'M', 'n':'N', 'o':'O', 'p':'P', 'q':'Q', 'r':'R', 's':'S', 't':'T', 'u':'U', 'v':'V', 'w':'W', 'x':'X', 'y':'Y', 'z':'Z'}   
    word = str(input())
    if word[0] in low_to_up.keys():
        word = low_to_up[word[0]]+word[1:]
    print (word)
    
    
    
    
if __name__ == '__main__':
    word_capitalization()
    