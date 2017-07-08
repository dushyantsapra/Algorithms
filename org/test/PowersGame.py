'''
Created on Jun 2, 2017

@author: sapra
'''
if __name__ == '__main__':
    inputfile = open("/home/sapra/input.txt")
    test_count = int(inputfile.readline().strip())

    for _ in range(test_count):
        power_range = int(inputfile.readline().strip())
        print("SECOND" if power_range % 8 == 0 else "FIRST")
        
        
        
        
