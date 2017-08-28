def petya_and_strings():
    str1 = str(input())
    str2 = str(input())
    up_to_low = {'A':'a', 'B':'b', 'C':'c', 'D':'d', 'E':'e', 'F':'f', 'G':'g', 'H':'h', 'I':'i', 'J':'j', 'K':'k', 'L':'l', 'M':'m', 'N':'n', 'O':'o', 'P':'p', 'Q':'q', 'R':'r', 'S':'s', 'T':'t', 'U':'u', 'V':'v', 'W':'w', 'X':'x', 'Y':'y', 'Z':'z'}
    order = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i, letter in enumerate(str1):
        if letter in up_to_low.keys():
            str1  = str1[:i] + up_to_low[letter] + str1[i+1:]
    for i, letter in enumerate(str2):
        if letter in up_to_low.keys():
            str2  = str2[:i] + up_to_low[letter] + str2[i+1:]
    
    l = len(str1)
    
    for i in range(0, l):
        letter1 = str1[i]
        letter2 = str2[i]
        if letter1 != letter2:
            ord1 = order.index(letter1)
            ord2 = order.index(letter2)
            if ord1 < ord2:
                print('-1')
                return
            else:
                print('1')
                return
    print('0')
                
        
        
                 
                           
       
    

if __name__ == '__main__':
    petya_and_strings()
    