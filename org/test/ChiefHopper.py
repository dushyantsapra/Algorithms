'''
Created on Jun 6, 2017

@author: xdussap
'''
from os.path import os


if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);
    
    arr_len = int(inputfile.readline().strip())
    
    arr = list(map(int, inputfile.readline().strip().split(" ")))
    
    energy_needed = arr[0]
    current_energy = 0
    
    iLoop = 1
    while iLoop < arr_len:
        if current_energy < arr[iLoop]:
            current_energy = arr[iLoop] - current_energy;
            if current_energy < 0:
                energy_needed += abs(current_energy)
                current_energy = 0
        else:
            current_energy += current_energy - arr[iLoop]
        iLoop += 1
    print(energy_needed)
