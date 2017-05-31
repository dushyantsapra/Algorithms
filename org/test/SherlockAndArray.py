'''
Created on May 30, 2017

@author: xdussap
'''
from os.path import os


if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);
    
    testCount = int(inputfile.readline().strip())

    for _ in range(testCount):
        arr_len = int(inputfile.readline().strip())
        arr = list(map(int, inputfile.readline().strip().split(" ")));
        
        if arr_len == 1:
            print("YES")
            continue

        arr_sum = 0;
        for e in arr:
            arr_sum += e;

        iLoop = 1
        
        is_possible = False
        previous_sum = 0;
        while iLoop < arr_len - 1:
            previous_sum += arr[iLoop - 1]
            if previous_sum == (arr_sum - previous_sum - arr[iLoop]):
                is_possible = True
                break
            iLoop += 1
            
        if is_possible:
            print("YES")
        else:
            print("NO")
            
            