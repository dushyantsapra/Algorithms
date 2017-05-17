'''
Created on Apr 21, 2017

@author: xdussap
'''
from os.path import os


if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);

    testCount = int(inputfile.readline().strip());

    for _ in range(testCount):
        anagram = inputfile.readline().strip();

        strlength = len(anagram)
        mid = int(len(anagram) / 2)

        if strlength % 2 == 1:
            print(-1);
            continue;
        else:
            str1 = anagram[0 : mid];
            str2 = anagram[mid : len(anagram)];

        strMap = {}

        for schar in str1:
            if schar not in strMap:
                strMap[schar] = 1;
            else:
                strMap[schar] += 1;

        notFoundCount = 0;
        for schar in str2:
            if schar not in strMap or strMap[schar] == 0 :
                notFoundCount += 1;
            else:
                strMap[schar] -= 1;

        remainingCount = 0;

        for value in strMap.values():
            remainingCount += value;
        
        if notFoundCount == remainingCount:
            print(notFoundCount);
        else:
            print(-1);