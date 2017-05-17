'''
Created on Apr 18, 2017

@author: xdussap
'''
from os.path import os

def get_avail_options(rowIndex, colIndex, matrix, currentPosition):
    availMoves = [];
    
    for proposedposition in range(4):
        if currentPosition == proposedposition:
            continue;
        if proposedposition == 0 and colIndex - 1 >= 0 and matrix[rowIndex][colIndex - 1] != 'X':
            availMoves.append(proposedposition);
        elif proposedposition == 1 and rowIndex - 1 >= 0 and matrix[rowIndex - 1][colIndex] != 'X':
            availMoves.append(proposedposition);
        elif proposedposition == 2 and (colIndex + 1) <= (len(matrix[0]) - 1) and matrix[rowIndex][colIndex + 1] != 'X':
            availMoves.append(proposedposition);
        elif proposedposition == 3 and (rowIndex + 1) <= (len(matrix) - 1) and matrix[rowIndex + 1][colIndex] != 'X':
            availMoves.append(proposedposition);
    return availMoves;

def check_if_possible(rowIndex, colIndex, matrix, moveCount, currentPosition):
#     if moveCount == 0:
#         return False;
    if matrix[rowIndex][colIndex] == '*':
        if moveCount == 0:
            return True;
        else:
            return False;

    availMoves = get_avail_options(rowIndex, colIndex, matrix, currentPosition);
    
    if moveCount == 0 and len(availMoves) > 1:
        return False
    
    for nextMove in availMoves:
        if nextMove == 0:
            if check_if_possible(rowIndex, colIndex - 1, matrix, (moveCount - 1) if len(availMoves) > 1 else moveCount, 2):
                return True;
        elif nextMove == 1:
            if check_if_possible(rowIndex - 1, colIndex, matrix, (moveCount - 1) if len(availMoves) > 1 else moveCount, 3):
                return True
        elif nextMove == 2:
            if check_if_possible(rowIndex, colIndex + 1, matrix, (moveCount - 1) if len(availMoves) > 1 else moveCount, 0):
                return True
        elif nextMove == 3:
            if check_if_possible(rowIndex + 1, colIndex, matrix, (moveCount - 1) if len(availMoves) > 1 else moveCount, 1):
                return True 
    return False

if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);

    testcount = int(inputfile.readline().strip());

    for _ in range(testcount):
        rowCount, columnCount = list(map(int, inputfile.readline().strip().split(" ")));

        matrix = [];
        rowIndex = -1;
        colIndex = -1;
        for index in range(rowCount):
            ll = list(inputfile.readline().strip());
            if 'M' in ll and rowIndex == -1 and colIndex == -1:
                rowIndex = index;
                colIndex = ll.index('M');
            matrix.append(ll);

#         print(matrix)
        
        movecount = int(inputfile.readline().strip());
        
#         print(movecount)
        
        if check_if_possible(rowIndex, colIndex, matrix, movecount, -1):
            print("Impressed")
        else:
            print("Oops!")
        