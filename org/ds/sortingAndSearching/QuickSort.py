'''
Created on 15-Jun-2016

@author: Dushyant
'''
from org.competitiveProgramming.Utility import Utility


class QuickSort:
    def quickSortPartition(self, sIndex, eIndex, orgList):
        pivot = orgList[eIndex];
        iValue = sIndex - 1;
        for jValue in range(sIndex, eIndex):
            if orgList[jValue] < pivot:
                iValue += 1;
                if iValue != jValue:
                    Utility.swap(iValue, jValue, orgList);
        Utility.swap((iValue + 1), eIndex, orgList);
        return (iValue + 1);

    def quickSortHelper(self, sIndex, eIndex, orgList):
        if(sIndex < eIndex):
            pivotIndex = self.quickSortPartition(sIndex, eIndex, orgList);
            self.quickSortPartition(sIndex, pivotIndex - 1, orgList);
            self.quickSortPartition(pivotIndex + 1, eIndex, orgList);
            return None;

    def quickSort(self, tempList):
        self.quickSortHelper(0, len(tempList) - 1, tempList);

        print("Quick Sort");
        for value in tempList:
            print(value);
        return None;

tempList = [6, 5, 3, 1, 8, 7, 2, 4];
sort = QuickSort();
sort.quickSort(tempList);
