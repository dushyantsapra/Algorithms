'''
Created on May 31, 2017

@author: sapra
'''

if __name__ == '__main__':
    inputfile = open("/home/sapra/input.txt");
    game_count = int(inputfile.readline().strip())
    
    for _ in range(game_count):
        towers, height = list(map(int, inputfile.readline().strip().split(" ")))
        
        print("2" if height == 1 or towers % 2 == 0 else "1")