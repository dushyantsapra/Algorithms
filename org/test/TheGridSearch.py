'''
Created on May 17, 2017

@author: xdussap
'''
from os.path import os


def computeSuffixWhichIsPrefixOfGivenString(string):
    stringLength = len(string);
    suffixPrefixArray = [0] * stringLength;

    if stringLength == 1:
        return suffixPrefixArray;

    iLoop = 0;
    jLoop = 1;
    while jLoop < stringLength:
        if string[iLoop] == string[jLoop]:
            suffixPrefixArray[jLoop] = iLoop + 1;
            iLoop += 1;
            jLoop += 1;
        else:
            if iLoop == 0:
                suffixPrefixArray[jLoop] = 0;
                jLoop += 1;
            else:
                iLoop = suffixPrefixArray[iLoop - 1];
    return suffixPrefixArray;

def kmpAlgo(mainString, subString, suffixPrefixArray):
#     suffixPrefixArray = computeSuffixWhichIsPrefixOfGivenString(subString);

    iLoop = 0;
    jLoop = 0;

    mainStringLength = len(mainString);
    subStringLength = len(subString);

    while iLoop < mainStringLength and jLoop < subStringLength:
        if mainString[iLoop] == subString[jLoop]:
            iLoop += 1;
            jLoop += 1;
        else:
            if jLoop == 0:
                iLoop += 1;
            else:
                jLoop = suffixPrefixArray[jLoop - 1];

    if jLoop == len(subString):
        return True
    else:
        return False

if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);

    testCount = int(inputfile.readline().strip());
    matrix = [];
    for _ in range(testCount):
        R, C = list(map(int, inputfile.readline().strip().split(" ")));
        for _ in range(R):
            matrix.append(inputfile.readline().strip());
        
        findMatrix = [];
        suffixPrefixArrayList = []
        r, c = list(map(int, inputfile.readline().strip().split(" ")));
        for _ in range(r):
            subString = inputfile.readline().strip()
            findMatrix.append(subString)
            suffixPrefixArrayList.append(computeSuffixWhichIsPrefixOfGivenString(subString));
        
        i = 0;
        j = 0;
        foundIndex = -1;
        while i < R and j < r:
            if kmpAlgo(matrix[i], findMatrix[j], suffixPrefixArrayList[j]):
                if foundIndex == -1:
                    foundIndex = i;
                j += 1;
                i += 1;
            else:
                if foundIndex != -1:
                    i = foundIndex + 1;
                else:
                    i += 1;
                j = 0;

        if j == r:
            print("YES")
        else:
            print("NO")
            
                
            




