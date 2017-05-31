'''
Created on May 26, 2017

@author: xdussap
'''
from os.path import os


def rotateMatrixByNPosition(numOfRotation, currentIndex, rowIndex, colIndex, rowCount, colCount, originalMatrix, rotatedMatrix):
    if numOfRotation <= 0:
        return
    if rowIndex == currentIndex:
        # Corner Case
        if colIndex == currentIndex:
            if numOfRotation > ((rowCount - currentIndex - 1) - rowIndex):
                rotatedMatrix[rowCount - currentIndex - 1][colIndex] = originalMatrix[rowIndex][colIndex]
                return rotateMatrixByNPosition((numOfRotation - ((rowCount - currentIndex - 1) - rowIndex)), currentIndex, (rowCount - currentIndex - 1), colIndex, rowCount, colCount, originalMatrix, rotatedMatrix)
            else:
                rotatedMatrix[rowIndex + numOfRotation][colIndex] = originalMatrix[rowIndex][colIndex]
                return
        # Corner Case
        elif colIndex == (colCount - currentIndex - 1):
            if numOfRotation > ((colCount - currentIndex - 1) - colIndex):
                rotatedMatrix[rowIndex][colCount - currentIndex - 1] = originalMatrix[rowIndex][colIndex]
                return rotateMatrixByNPosition((numOfRotation - (colCount - currentIndex - 1) - colIndex), currentIndex, rowIndex, (colIndex - currentIndex - 1), rowCount, colCount, originalMatrix, rotatedMatrix)
            else:
                rotatedMatrix[rowIndex][rowIndex + numOfRotation] = originalMatrix[rowIndex][colIndex]
                return
        else:
            pass
    elif rowIndex == (rowCount - currentIndex - 1):
        # Corner Case
        if colIndex == currentIndex:
            pass
        # Corner Case
        elif colIndex == (colCount - currentIndex - 1):
            pass
        else:
            pass

if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);
    n, m, rotations = list(map(int, inputfile.readline().strip().split(" ")));
    
    matrix = [];
    for _ in range(n):
        matrix.append(list(map(int, inputfile.readline().strip().split(" "))))
    
    print(matrix)
    
    outerLoopLen = int(n / 2)
    for currentIndex in range(outerLoopLen):
        digitCount = ((n - (currentIndex * 2)) * 2) + (((m - 2) - (currentIndex * 2)) * 2)
        rotationCount = rotations % digitCount;
        for iLoop in range(currentIndex, n):
            for jLoop in range(currentIndex, m):
                if iLoop == currentIndex:
                    pass
                elif iLoop == (n - currentIndex):
                    pass
