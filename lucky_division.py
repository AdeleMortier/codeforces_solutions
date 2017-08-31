def is_lucky(number):
    number = str(number)
    for digit in number:
        if not(digit == '4' or digit == '7'):
            return False
    return True
    

def lucky_division():
    number = int(input())
    if number <= 0:
        print ('NO')
        return
    if is_lucky(number):
        print ('YES')
        return
    else:
        lucky_divisors = [i for i in range(2, number) if is_lucky(i)]
        for i in lucky_divisors:
            if number % i == 0:
                print ('YES')
                return
    print('NO')
        

if __name__ == '__main__':
    lucky_division()
