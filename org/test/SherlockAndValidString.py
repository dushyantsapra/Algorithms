'''
Created on Apr 24, 2017

@author: xdussap
'''
from os.path import os


def checkIfStringValid(inputString):
    charCountMap = {};

    for schar in inputString:
        if schar in charCountMap:
            charCountMap[schar] += 1;
        else:
            charCountMap[schar] = 1;
    
    print(charCountMap)

    countcharMap = {};
    uniqueValue = [];
    for key, value in charCountMap.items():
        if value in countcharMap: 
            countcharMap[value].append(key);
        else:
            countcharMap[value] = [key];
            uniqueValue.append(value);

    uniqueValue = sorted(uniqueValue)

    print(countcharMap)
    print(uniqueValue)

    if len(countcharMap) == 1:
        print("YES")
    elif len(countcharMap) == 2 and (len(countcharMap[uniqueValue[0]]) == 1 or len(countcharMap[uniqueValue[1]]) == 1):
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);

    testString = inputfile.readline().strip();
    checkIfStringValid(testString)
