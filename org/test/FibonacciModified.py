'''
Created on Jun 4, 2017

@author: sapra
'''

def fibonacci_number(computed_result, n):
    if n in computed_result:
        return computed_result[n]
    
    computed_result[n] = fibonacci_number(computed_result, n - 1) ** 2 + fibonacci_number(computed_result, n - 2)
    return computed_result[n]

if __name__ == '__main__':
    inputfile = open("/home/sapra/input.txt")
    t1, t2, n = list(map(int, inputfile.readline().strip().split(" ")))
    
    computed_result = {}
    
    computed_result[0] = t1
    computed_result[1] = t2
    
    print(fibonacci_number(computed_result, n - 1))    