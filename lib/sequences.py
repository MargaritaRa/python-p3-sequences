#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([]) 
        return
    
    
    fib_sequence = [0, 1]
    
    if length == 1:
        print([0])  
        return
    elif length == 2:
        print([0, 1]) 
        return
    
    
    while len(fib_sequence) < length:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    
   
    print(fib_sequence)


print_fibonacci(0)  
print_fibonacci(1)  
print_fibonacci(2) 
print_fibonacci(5) 
print_fibonacci(10) 
