'''
Created on Apr 7, 2017

@author: xdussap
'''
from os.path import os
import re


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

def kmpAlgo(mainString, subString):
    suffixPrefixArray = computeSuffixWhichIsPrefixOfGivenString(subString);

    iLoop = 0;
    jLoop = 0;

    mainStringLength = len(mainString);
    subStringLength = len(subString);

    start_index = 0;
    while iLoop < mainStringLength and jLoop < subStringLength:
        if mainString[iLoop] == subString[jLoop]:
            iLoop += 1;
            jLoop += 1;
        else:
            if jLoop == 0:
                iLoop += 1;
            else:
                jLoop = suffixPrefixArray[jLoop - 1];
            start_index = iLoop;

    if jLoop == len(subString):
        return start_index;
    else:
        return -1;

"""\
# No Working
if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);

    test_Count = int(inputfile.readline().strip());

    for _ in range(test_Count):
        matrix_row_count, matrix_column_count = inputfile.readline().strip().split();
        matrix_row_count, matrix_column_count = int(matrix_row_count), int(matrix_column_count);

        matrix = [];

        for row_index in range(matrix_row_count):
            matrix.insert(row_index, inputfile.readline().strip());

        sub_matrix_row_count, sub_matrix_column_count = inputfile.readline().strip().split();
        sub_matrix_row_count, sub_matrix_column_count = int(sub_matrix_row_count), int(sub_matrix_column_count);

        find_matrix = [];
        for row_index in range(sub_matrix_row_count):
            find_matrix.insert(row_index, inputfile.readline().strip());

#         print(matrix);
#         print(find_matrix);

        matrix_index = 0;
        sub_matrix_index = 0;
        is_sub_matrix = False;
        while matrix_index < len(matrix):
            start_column_index = kmpAlgo(matrix[matrix_index], find_matrix[sub_matrix_index]);
            if start_column_index == -1:
                matrix_index += 1;
                continue;
            else:
                matrix_temp_index = matrix_index + 1;
                sub_matrix_temp_index = 1;
                while sub_matrix_temp_index < len(find_matrix):
                    temp_index = kmpAlgo(matrix[matrix_temp_index], find_matrix[sub_matrix_temp_index]);
                    if temp_index == -1 or temp_index != start_column_index:
                        matrix_index += 1;
                        sub_matrix_index = 0;
                        break;
                    else:
                        matrix_temp_index += 1;
                        sub_matrix_temp_index += 1;
                if sub_matrix_temp_index == len(find_matrix):
                    is_sub_matrix = True;
                    break;

        if is_sub_matrix:
            print("YES");
        else:
            print("NO");"""

"""if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);

    test_Count = int(inputfile.readline().strip());

    for _ in range(test_Count):
        matrix_row_count, matrix_column_count = inputfile.readline().strip().split();
        matrix_row_count, matrix_column_count = int(matrix_row_count), int(matrix_column_count);

        matrix = [];

        for row_index in range(matrix_row_count):
            matrix.insert(row_index, inputfile.readline().strip());

        sub_matrix_row_count, sub_matrix_column_count = inputfile.readline().strip().split();
        sub_matrix_row_count, sub_matrix_column_count = int(sub_matrix_row_count), int(sub_matrix_column_count);

        find_matrix = [];
        for row_index in range(sub_matrix_row_count):
            find_matrix.insert(row_index, inputfile.readline().strip());

        print(matrix)
        print(find_matrix)
    
        
        matrix_row_index = 0;
        matrix_column_index = 0;
        sub_matrix_row_index = 0;
        sub_matrix_column_index = 0;
        
        while matrix_row_index < len(matrix):
            if matrix[matrix_row_index][matrix_column_index] == find_matrix[sub_matrix_row_index][sub_matrix_column_index]:
                temp_matrix_row_index = matrix_row_index + 1;
                temp_matrix_column_index = 0;
                temp_sub_matrix_row_index = sub_matrix_row_index + 1;
                temp_sub_matrix_column_index = 0;
"""


if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    """with open(path) as f:
        for line in f:
            if re.match("(.*)JOURNAL_DIRECTORY" + "(.*)", line):
                print(line.index("JOURNAL_DIRECTORY"))

                print (line),"""
    
#     pattern = re.compile("(.*)key(.*)")
#     for i, line in enumerate(open(path)):
#         for match in re.finditer(pattern, line):
#             print ('Found on line %s: %s' % (i+1, match.groups(2)))

    regex = r'\b\w+\b'
    with open(path) as f:
        for line in f:
            list1=re.findall(regex,line)
            print (list1),
    
    

