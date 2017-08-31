def queue_at_the_school():
    queue_size, steps = input().split()
    steps = int(steps)
    queue_size = int(queue_size)
    queue = input()
    
    for i in range(0, steps):
        i = 0
        while i < queue_size - 1:
            if queue[i:i+2] == 'BG':
                queue = queue[:i] + 'GB' + queue[i+2:]
                i += 1
            i += 1
    print(queue)
                
    
if __name__ == '__main__':
    queue_at_the_school()