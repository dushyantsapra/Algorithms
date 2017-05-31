'''
Created on May 30, 2017

@author: sapra
'''

def get_recursive_digit_sum(p):
    if p % 10 == p:
        return p
    
    recursive_sum = 0;
    
    while p > 0:
        recursive_sum += int(p % 10)
        p = int(p / 10)
    return get_recursive_digit_sum(recursive_sum)

if __name__ == '__main__':
    inputfile = open("/home/sapra/input.txt");
    n, k = list(inputfile.readline().strip().split(" "))
    k = int(k)
    digits = list(n)
     
    recursive_sum = 0
    for digit in digits:
        recursive_sum += int(digit);
    
    recursive_sum *= k
     
    print(get_recursive_digit_sum(recursive_sum))
    
    