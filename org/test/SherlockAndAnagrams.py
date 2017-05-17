'''
Created on Apr 24, 2017

@author: xdussap
'''
import math


def printSubsequences(arr, n):
    opsize = int(math.pow(2, n));
 
    ll = [];
    for iLoop in range(1, opsize):
        templist = []
        for jLoop in range(opsize):
            if iLoop & int(1 << jLoop):
#                 print(arr[jLoop], end=" ");
                templist.append(arr[jLoop])
#         print();
        ll.append(sorted(templist));
    print(ll)
    
    countmap = {};
    anagramCount = 0;
    for tempList in ll:
        tempStr = ''.join(tempList);
        if tempStr in countmap:
            anagramCount += 1;
        else:
            countmap[tempStr] = 1;
    
    print(anagramCount)

if __name__ == '__main__':
    printSubsequences(list("ifailuhkqq"), 10)
