'''
Created on Apr 10, 2017

@author: xdussap
'''
from os.path import os

def is_array_sorted(sortedarr):
    curIndex = 1;
    
    while curIndex < len(sortedarr):
        if sortedarr[curIndex] > sortedarr[curIndex - 1]:
            pass;
        else:
            return False
        curIndex += 1;
    return True; 

if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);

    
    arr_len = int(inputfile.readline().strip());
    arr = list(map(int, inputfile.readline().strip().split(" ")));

    is_first = True;
    index_arr = [];
    i = 1;
    while i < arr_len:
        if arr[i] < arr[i - 1]:
            if is_first:
                index_arr.append(i - 1)
                is_first = False;
            index_arr.append(i)
        i += 1;
    print(index_arr);
    
    if len(index_arr) == 0:
        print("yes")
    elif len(index_arr) == 2 or len(index_arr) == 3:
        sIndex = 0;
        if len(index_arr) == 2:
            eIndex = 1;
        else:
            eIndex = 2;
        arr[index_arr[sIndex]], arr[index_arr[eIndex]] = arr[index_arr[eIndex]], arr[index_arr[sIndex]];
        if  is_array_sorted(arr):
            print("yes")
            if len(index_arr) == 2:
                print("swap {} {}".format(index_arr[sIndex] + 1, index_arr[eIndex] + 1))
            else:
                if index_arr[2] - index_arr[0] == 2: 
                    print("reverse {} {}".format(index_arr[sIndex] + 1, index_arr[eIndex] + 1))
                else:
                    print("swap {} {}".format(index_arr[sIndex] + 1, index_arr[eIndex] + 1))
        else:
            print("no")
    else:
        iLoop = 1;
        is_valid = True;
        while iLoop < len(index_arr):
            if index_arr[iLoop] - index_arr[iLoop - 1] > 1:
                is_valid = False;
                break;
            iLoop += 1;
        if not is_valid:
            print("no")
        else:
            print("yes")
            print("reverse {} {}".format(index_arr[0] + 1, index_arr[len(index_arr) - 1] + 1));




