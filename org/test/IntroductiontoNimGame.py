'''
Created on Jun 2, 2017

@author: sapra
'''

if __name__ == '__main__':
    inputfile = open("/home/sapra/input.txt")
    test_count = int(inputfile.readline().strip())
    for _ in range(test_count):
        pile_count = int(inputfile.readline().strip())
        
        nim_sum = 0
        
        piles = list(map(int, inputfile.readline().strip().split(" ")))
        for pile in piles:
            nim_sum ^= pile
        
        print("First" if nim_sum != 0 else "Second")