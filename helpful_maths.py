def helpful_maths():
    addition = str(input())
    addition = addition.split("+")
    addition = [int(summand) for summand in addition]
    addition = sorted(addition)
    new_addition = ''
    for summand in addition:
        new_addition += str(summand)+'+'
    
    print(new_addition[:-1])


if __name__ == '__main__':
    helpful_maths()
    