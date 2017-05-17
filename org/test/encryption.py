'''
Created on Apr 17, 2017

@author: xdussap
'''
import math
from os.path import os

if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);
  
    inputstring = inputfile.readline().strip();
  
    strlen = len(inputstring);
  
    matrixcolumn = int(math.ceil(math.sqrt(strlen)));

    matrixrow = int(strlen / matrixcolumn);
      
    isExtra = False if int(matrixrow * matrixcolumn) >= strlen else True
    
    if isExtra:
        matrixrow += 1;
    matrixSize = matrixrow * matrixcolumn;
    
    matrix = [];
    for iLoop in range(matrixrow):
        matrix.append(inputstring[iLoop * matrixcolumn : (iLoop + 1) * matrixcolumn])

    isExtra = False if int(matrixrow * matrixcolumn) >= strlen else True

    if isExtra:
        matrix.append(inputstring[matrixrow * matrixcolumn : strlen])

    rowcount = len(matrix);
    columncount = len(matrix[0]);
#     print(matrix)

    rowcurrentcount = 0;
    for colindex in range(columncount):
        ll = [];
        for rowindex in range(rowcount):
            if len(matrix[rowindex]) >= colindex + 1:
                ll.append(matrix[rowindex][colindex])
            else:
                break;
        print(''.join(ll), end=' ');