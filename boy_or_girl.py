def boy_or_girl():
    name = str(input())
    name = [letter for letter in name]
    letters = set(name)
    n_letters = len(letters)
    if n_letters % 2 == 0:
        print ('CHAT WITH HER !')
    else:
        print('IGNORE HIM !')
    
    
if __name__ == '__main__':
    boy_or_girl()
    