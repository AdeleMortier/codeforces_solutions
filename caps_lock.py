def caps_lock():
    up_to_low = {'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f', 'G':'g', 'H':'h', 'I':'i', 'J':'j', 'K':'k', 'L':'l', 'M':'m', 'N':'n', 'O':'o', 'P':'p', 'Q':'q', 'R':'r', 'S':'s', 'T':'t', 'U':'u', 'V':'v', 'W':'w', 'X':'x', 'Y':'y', 'Z':'z'}
    low_to_up = {'a':'A', 'b':'B', 'c':'C', 'd':'D', 'e':'E', 'f':'F', 'g':'G', 'h':'H', 'i':'I', 'j':'J', 'k':'K', 'l':'L', 'm':'M', 'n':'N', 'o':'O', 'p':'P', 'q':'Q', 'r':'R', 's':'S', 't':'T', 'u':'U', 'v':'V', 'w':'W', 'x':'X', 'y':'Y', 'z':'Z'}
    word = str(input())

    for i, letter in enumerate(word):
        if letter not in up_to_low.keys() and i != 0:
            print (word)
            return
    
    for i, letter in enumerate(word):
        if letter in up_to_low.keys():
            word = word[:i] + up_to_low[letter] + word[i+1:]
        else:
            word = word[:i] + low_to_up[letter] + word[i+1:]
    print(word)
    
    
if __name__ == '__main__':
    caps_lock()
    
        
        
    