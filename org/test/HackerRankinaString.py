'''
Created on May 5, 2017

@author: xdussap
'''
from os.path import os


if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);

    testcount = int(inputfile.readline().strip());
    
    findString = ['h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k'];
    for _ in range(testcount):
        isPresent = False;
        currentIndex = 0;
        mainString = inputfile.readline().strip()
        for c in mainString:
            if c == findString[currentIndex]:
                currentIndex += 1;
            
            if currentIndex == len(findString):
                isPresent = True;
                break;
    
        if isPresent:
            print("YES")
        else:
            print("NO")
