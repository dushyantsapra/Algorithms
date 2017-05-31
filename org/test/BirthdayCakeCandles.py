'''
Created on May 29, 2017

@author: xdussap
'''
from os.path import os


if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);
    
    arrLen = int(inputfile.readline().strip())
    arr = list(map(int, inputfile.readline().strip().split(" ")));
    
    maxValue = float("-inf");
    
    frequencyMap = {};
    
    for element in arr:
        if element > maxValue:
            maxValue = element
        if element in frequencyMap:
            frequencyMap[element] += 1;
        else:
            frequencyMap[element] = 1;
            
    print(frequencyMap[maxValue])