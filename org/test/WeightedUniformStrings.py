'''
Created on May 5, 2017

@author: xdussap
'''
from os.path import os


if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);
    
    mainString = inputfile.readline().strip()
#     print(mainString)
    strLen = len(mainString);

    opMap = {int(ord(mainString[0]) - 97 + 1) : True};
    currenchar = mainString[0];
    currentCount = 1
    for index in range(1, strLen):
        if mainString[index] == currenchar:
            currentCount += 1
        else:
            currentCount = 1
        currenchar = mainString[index];
        opMap[int((ord(mainString[index]) - 97 + 1) * currentCount)] = True;
    
#     print(opMap)
        
    testcount = int(inputfile.readline().strip());
    
    for _ in range(testcount):
        testvalue = int(inputfile.readline().strip());
        if testvalue in opMap:
            print("Yes")
        else:
            print("No")
            
            