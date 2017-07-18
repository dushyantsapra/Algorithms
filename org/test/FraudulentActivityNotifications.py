'''
Created on Jun 6, 2017

@author: xdussap
'''
from os.path import os


if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);
    arr_len, k = list(map(int, inputfile.readline().strip().split(" ")))

    arr = list(map(int, inputfile.readline().strip().split(" ")))

#     print("{}, {}, {}".format(arr_len, k, arr))

    start_index = 0
    index = k
    sorted_arr = sorted(arr[start_index: start_index + k])
    is_even = True if k % 2 == 0 else False
    
    fradulent_activity_count = 0
    while index < arr_len:
        mid_index = int(k / 2)
        if is_even:
            if sorted_arr[mid_index] + sorted_arr[mid_index - 1] * 2 <= arr[index]:
                fradulent_activity_count += 1
        else:
            if sorted_arr[int(k / 2)] * 2 <= arr[index]:
                fradulent_activity_count += 1
        
        index += 1
        start_index += 1
        sorted_arr = sorted(arr[start_index: start_index + k])
    
    print(fradulent_activity_count)
