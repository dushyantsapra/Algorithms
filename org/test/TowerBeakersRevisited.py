'''
Created on May 31, 2017

@author: sapra
'''

if __name__ == '__main__':
    inputfile = open("/home/sapra/input.txt");
    game_count = int(inputfile.readline().strip())
    
    for _ in range(game_count):
        towers = int(inputfile.readline().strip())
        heights = list(map(int, inputfile.readline().strip().split(" ")))
        
        icount = 0
        
        for height in heights:
            if height > 1:
                icount += 1
        print("2" if icount % 2 == 0 else "1")