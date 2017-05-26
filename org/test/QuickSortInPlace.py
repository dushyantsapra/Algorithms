'''
Created on May 17, 2017

@author: xdussap
'''
from os.path import os


def quickSortPartition(sIndex, eIndex, orgList):
    pivot = orgList[eIndex];
    iValue = sIndex - 1;
    for jValue in range(sIndex, eIndex):
        if orgList[jValue] <= pivot:
            iValue += 1;
            orgList[iValue], orgList[jValue] = orgList[jValue], orgList[iValue] 
    iValue += 1;
    orgList[iValue], orgList[eIndex] = orgList[eIndex], orgList[iValue]
    print(*orgList, sep=' ')
#     print(orgList)
    return iValue;

def quickSortHelper(sIndex, eIndex, orgList):
    if(sIndex < eIndex):
        pivotIndex = quickSortPartition(sIndex, eIndex, orgList);
        quickSortHelper(sIndex, pivotIndex - 1, orgList);
        quickSortHelper(pivotIndex + 1, eIndex, orgList);

if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);

    arrlength = int(inputfile.readline().strip());
    arr = list(map(int, inputfile.readline().strip().split(" ")));
    
    quickSortHelper(0, arrlength - 1, arr)
