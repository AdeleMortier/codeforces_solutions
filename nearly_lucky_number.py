def nearly_lucky_number():
    number = str(input())
    lucky_digits = [i for i in number if (int(i) == 7 or int(i) == 4)]
    n_lucky = len(lucky_digits)
    if n_lucky == 7 or n_lucky == 4:
        print ('YES')
    else:
        print ('NO')
    
if __name__ == '__main__':
    nearly_lucky_number()