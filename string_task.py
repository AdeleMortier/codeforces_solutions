def string_task():
    word = str(input())
    vowels = ['A', 'E', 'I', 'O', 'U', 'Y', 'a', 'e', 'i', 'o', 'u', 'y']
    up_to_low = {'B':'b', 'C':'c', 'D':'d', 'F':'f', 'G':'g', 'H':'h', 'J':'j', 'K':'k', 'L':'l', 'M':'m', 'N':'n', 'P':'p', 'Q':'q', 'R':'r', 'S':'s', 'T':'t', 'V':'v', 'W':'w', 'X':'x', 'Z':'z'}
    end = len(word)
    i = 0
    while i < end:
        letter = word[i]
        if letter in up_to_low.keys():
            word = word[:i] + up_to_low[letter] + word[i+1:]
        if letter in vowels:
            word = word[:i]+word[i+1:]
            end -=1
            i -= 1
        else:
            word = word[:i]+'.'+word[i:]
            end += 1
            i +=1
      
        i += 1
    print(word)
           
    
if __name__ == '__main__':
    string_task()
    