'''
Created on Jun 9, 2017

@author: sapra
'''


def fibonacci_number(computed_result, n):
    if n in computed_result:
        return computed_result[n]
    
    computed_result[n] = fibonacci_number(computed_result, n - 1) + fibonacci_number(computed_result, n - 2)
    return computed_result[n]

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x 

if __name__ == '__main__':
    inputfile = open("/home/sapra/input.txt")
    n, test_count = list(map(int, inputfile.readline().strip().split(" ")))
    num_arr = list(map(int, inputfile.readline().strip().split(" ")))
    
    computed_result = {}

    computed_result[0] = 0
    computed_result[1] = 1    
    for _ in range(test_count):
        l, r = list(map(int, inputfile.readline().strip().split(" ")))
        
        result = num_arr[l - 1]
        for iLoop in range(l, r):
            result = fibonacci_number(computed_result, gcd(num_arr[iLoop], result))

        print(result)
            
            
            
