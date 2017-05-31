'''
Created on May 31, 2017

@author: sapra
'''
from datetime import datetime


def isprime(n):
    """Returns True if n is prime."""
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True

if __name__ == '__main__':
    input_file = open("/home/sapra/input.txt");
    game_count = int(input_file.readline().strip())
    
    prime_count_map = {}
    
    print(datetime.now())
    current_count = 0
    for value in range(2, 100000 + 1):
        if isprime(value):
            current_count += 1;
        prime_count_map[value] = current_count
    
    print(datetime.now())
    
    for _ in range(game_count):
        n = int(input_file.readline().strip())
        
        if n == 1:
            print("Bob")
            continue
        
        print("Alice" if prime_count_map[n] % 2 == 1 else "Bob")
            
