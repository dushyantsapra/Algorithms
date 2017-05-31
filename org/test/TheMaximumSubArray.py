'''
Created on May 29, 2017

@author: xdussap
'''
from os.path import os


if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);

    testCount = int(inputfile.readline().strip())

    for _ in range(testCount):
        arrLen = int(inputfile.readline().strip())
        arr = list(map(int, inputfile.readline().strip().split(" ")));

        max_so_far = arr[0]
        curr_max = arr[0];
        for iLoop in range(1, arrLen):
            curr_max = max(arr[iLoop], curr_max + arr[iLoop])
            max_so_far = max(max_so_far, curr_max)
        
        non_continuous_sum = arr[0]
        for iLoop in range(1, arrLen):
            if arr[iLoop] > non_continuous_sum and non_continuous_sum < 0:
                non_continuous_sum = arr[iLoop];
            else:
                non_continuous_sum = max(non_continuous_sum, non_continuous_sum + arr[iLoop])

        print("{} {}".format(max_so_far, non_continuous_sum))