'''
Created on May 11, 2017

@author: xdussap
'''
from os.path import os


if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);

    houseCount, radioFrequencyRange = list(map(int, inputfile.readline().strip().split(" ")));

    housePositionArr = list(map(int, inputfile.readline().strip().split(" ")));
    housePositionArr = set(housePositionArr);
    housePositionArr = list(housePositionArr)
    housePositionArr = sorted(housePositionArr)
    
    houseCount = len(housePositionArr);

    currentCapacity = radioFrequencyRange;
    
    previousIndex = 0;
    litIndex = 0;
    
    index = 1;
    isBackward = True;
    isForward = False;
    iCount = 0;
    proposedIndex = -1
    while index < houseCount:
        if isBackward:
            if housePositionArr[index] - housePositionArr[previousIndex] <= radioFrequencyRange:
                litIndex = index;
                index += 1;
            else:
                proposedIndex = -1
                iCount += 1;
#                 print(litIndex)
                previousIndex = litIndex;
                isBackward = False;
                isForward = True;
        else:
            if housePositionArr[index] - housePositionArr[previousIndex] <= radioFrequencyRange:
                index += 1;
            else:
                proposedIndex = index;
                litIndex = index;
                previousIndex = index;
                isBackward = True;
                isForward = False;
                index += 1;
    
    if proposedIndex != -1 or iCount == 0:
        iCount += 1;
    print(iCount)
            



        
