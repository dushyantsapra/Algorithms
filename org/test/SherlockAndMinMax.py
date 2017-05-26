'''
Created on May 17, 2017

@author: sapra
'''
"""if __name__ == '__main__':
    print(datetime.now())
    for _ in range(70283784, 302962360):
        pass
    print(datetime.now())
    print("Hello")"""

from _datetime import datetime
from os.path import os


if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);
    arrLen = int(inputfile.readline().strip());
#     print(arrLen)
    
    originlArr = list(map(int, inputfile.readline().strip().split(" ")));
    originlArr = sorted(originlArr)
    originalArrMap = {};
    for e in originlArr:
        originalArrMap[e] = True
#     print(originlArr)

    startrange, endrange = list(map(int, inputfile.readline().strip().split(" ")));

    i = 0;
    mergedArr = [];
    currentIndex = 0
    elementIndexMap = {};
    while originlArr[i] < startrange:
        mergedArr.append(originlArr[i])
        currentIndex += 1;
        i += 1;

    for element in range(startrange, (endrange + 1)):
        mergedArr.append(element)
        if element not in originalArrMap:
            elementIndexMap[element] = currentIndex;
        else:
            i += 1;
        currentIndex += 1;

#     while i < arrLen and originlArr[i] <= endrange:
#         i += 1;

    while i < arrLen:
        mergedArr.append(originlArr[i])
#         elementIndexMap[originlArr[i]] = currentIndex;
        currentIndex += 1;
        i += 1;

#     print(mergedArr)
#     print(elementIndexMap)
    
    maxOfMin = float("-inf");
    mergedArrLen = len(mergedArr)
    minValueListMap = {};
    for element, index in elementIndexMap.items():
        currentMin = float("inf");
        tempIndex = index;
        while tempIndex > 0:
            if mergedArr[tempIndex - 1] not in elementIndexMap:
                currentMin = mergedArr[index] - mergedArr[tempIndex - 1];
                break
            tempIndex -= 1;
        tempIndex = index;
        while tempIndex < (mergedArrLen - 1): 
            if mergedArr[tempIndex + 1] not in elementIndexMap:
                diff = mergedArr[tempIndex + 1] - mergedArr[index]
                currentMin = currentMin if currentMin < diff else diff;
                break
            tempIndex += 1;
        
        if currentMin == 0:
            continue
        
        if currentMin not in minValueListMap:
            minValueListMap[currentMin] = [element]
        else:
            minValueListMap[currentMin].append(element);
        
        if maxOfMin < currentMin:
            maxOfMin = currentMin;
    
#     print(minValueListMap)
#     print(maxOfMin)
    
    print(sorted(minValueListMap[maxOfMin])[0])
    
    
    