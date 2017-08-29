def chat_room():
    word = str(input())
    hello = ['h', 'e', 'l', 'l', 'o']
    for letter in hello:
        if letter not in word:
            print('NO')
            return
    letter_to_find = hello[0]
    i = 0
    for letter in word:
        if letter == letter_to_find:
            i += 1
            if i == len(hello):
                print('YES')
                return
            letter_to_find = hello[i]
    print ('NO')
            
    
if __name__ == '__main__':
    chat_room()