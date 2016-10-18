'''
Created on 28-Jun-2016

@author: Dushyant Sapra
'''

from org.ds.tree.BinaryHeap import BinaryHeapUsingArray

class HeapSort:
    def heapify(self, tempList, binaryHeapType):
        if binaryHeapType is "MIN":
            binaryHeapObj = BinaryHeapUsingArray("MIN_HEAP");
        elif binaryHeapType is "MAX":
            binaryHeapObj = BinaryHeapUsingArray("MAX_HEAP");
        for num in tempList:
            binaryHeapObj.insert(num, num);

        return binaryHeapObj.binaryHeap;

    def heapSort(self, tempList, sortedList, sortType):
        if len(tempList) == 1:
            sortedList.append(tempList.pop(0));
            return;
        else:
            tempList = self.heapify(tempList, sortType);
            sortedList.append(tempList.pop(0));
            self.heapSort(tempList, sortedList, sortType);

tempList = [6, 5, 3, 1, 8, 7, 2, 4];
sortedList = [];
sort = HeapSort();
sort.heapSort(tempList, sortedList, "MAX");

print(sortedList)
