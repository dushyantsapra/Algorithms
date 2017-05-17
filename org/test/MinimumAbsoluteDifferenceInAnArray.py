'''
Created on Apr 24, 2017

@author: xdussap
'''
from os.path import os


if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);

    arrLength = int(inputfile.readline().strip());
    
    arr = sorted(list(map(int, inputfile.readline().strip().split(" "))));
    
    minimumValue = float("inf");
    for iLoop in range(arrLength):
        for jLoop in range(iLoop + 1, arrLength):
            if minimumValue > abs(arr[jLoop] - arr[iLoop]):
                minimumValue = abs(arr[jLoop] - arr[iLoop]);
    
    print(minimumValue)
            
    
#     if arrLength % 2 == 1:
#         midindex = int((arrLength - 1) / 2);
#         diff1 = arr[midindex + 1] - arr[midindex];
#         diff2 = arr[midindex] - arr[midindex - 1]
#         minimumValue = diff1 if diff1 < diff2 else diff2;
#     else:
#         midindex = int((arrLength) / 2);
#         minimumValue = (arr[midindex] - arr[midindex - 1]);
#     print(minimumValue)
        
 
