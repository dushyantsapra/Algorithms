'''
Created on May 26, 2017

@author: sapra
'''
from org.test.ConnectedCellsInGrid import colcount
from org.test.CountLuck import rowIndex

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
            if numOfRotation > (colIndex - currentIndex):
                rotatedMatrix[rowIndex][currentIndex] = originalMatrix[rowIndex][colIndex]
                return rotateMatrixByNPosition((numOfRotation - (colIndex - currentIndex)), currentIndex, rowIndex, currentIndex, rowCount, colCount, originalMatrix, rotatedMatrix)
            else:
                rotatedMatrix[rowIndex][colIndex - numOfRotation] = originalMatrix[rowIndex][colIndex]
                return
        else:
            if numOfRotation > (colIndex - currentIndex):
                rotatedMatrix[rowIndex][currentIndex] = originalMatrix[rowIndex][colIndex]
                return rotateMatrixByNPosition((numOfRotation - (colIndex - currentIndex)), currentIndex, rowIndex, currentIndex, rowCount, colCount, originalMatrix, rotatedMatrix)
            else:
                rotatedMatrix[rowIndex][colIndex - currentIndex] = originalMatrix[rowIndex][colIndex]
                return
    elif rowIndex == (rowCount - currentIndex - 1):
        # Corner Case
        if colIndex == currentIndex:
            pass
        # Corner Case
        elif colIndex == (colCount - currentIndex - 1):
            pass
        else:
            pass
    else:
        pass

if __name__ == '__main__':
    inputfile = open("/home/sapra/input.txt");
    n, m, rotations = list(map(int, inputfile.readline().strip().split(" ")));
   
    matrix = [];
    for _ in range(n):
        matrix.append(list(map(int, inputfile.readline().strip().split(" "))))
   
    print(matrix)
   
    outerLoopLen = int(n / 2)
    for currentIndex in range(outerLoopLen):
        digitCount = ((n - (currentIndex * 2)) * 2) + (((m - 2) - (currentIndex * 2)) * 2)
        rotationCount = rotations % digitCount;
        for rowIndex in range(currentIndex, n):
            for colIndex in range(currentIndex, m):
                for _ in range(rotationCount):
                    finalRowIndex = rowIndex;
                    finalColIndex = colIndex;
                    if rowIndex == (currentIndex + 1)  and colIndex >= currentIndex and colIndex <= (colcount - 1 - currentIndex):
                        finalColIndex -= 1;
                    elif rowIndex >= currentIndex and rowIndex <= (n - 1 - currentIndex - 1):
                        finalRowIndex += 1;
                         

                
