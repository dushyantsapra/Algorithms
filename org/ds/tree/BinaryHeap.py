'''
Created on 17-Jun-2016

@author: Dushyant
'''
"""A binary heap is a heap data structure created using a binary tree. 
    It can be seen as a binary tree with two additional constraints:
i) The shape property: the tree is a complete binary tree; that is, all levels of the tree, 
    except possibly the last one (deepest) are fully filled and if the last level of the tree is not complete, 
    the nodes of that level are filled from left to right.
ii) The heap property: each node is greater than or equal to each of its children according to a comparison 
    predicate defined for the data structure.
    
Note - while Deleting Heapify Down to Only subtree whose value is less/greater then the deleted node Value. 

"""

from org.competitiveProgramming.Utility import Utility

class BinaryHeapUsingArray:
    def __init__(self, treeType):
        self.treeTpye = treeType;
        self.binaryHeap = [];

    def traverseTree(self):
        for value in self.binaryHeap:
            print(value);

    def heapifyDown(self, index):
        length = len(self.binaryHeap);
        hasLeft = False;
        hasRight = False;
        minIndex = -1;
        maxIndex = -1;

#         Left Sub-Tree
        if ((2 * index) + 1) <= (length - 1):
            hasLeft = True;
            leftIndex = (2 * index) + 1;
#         Right Sub-Tree
        if ((2 * index) + 1 + 1) <= (length - 1):
            hasRight = True;
            rightIndex = (2 * index) + 1 + 1;

        if "MIN_HEAP" is self.treeTpye:
            if hasLeft and hasRight:
                minIndex = leftIndex if self.binaryHeap[leftIndex] < self.binaryHeap[rightIndex] else rightIndex;
            elif hasLeft:
                minIndex = leftIndex;
            elif hasRight:
                minIndex = rightIndex;
            
            if minIndex != -1:
                if self.binaryHeap[minIndex] < self.binaryHeap[index]:
                    Utility.swapUsingTempVariable(minIndex, index, self.binaryHeap);
                    return  self.heapifyDown(minIndex);
                else:
                    return;
            else:
                return;
        elif "MAX_HEAP" is self.treeTpye:
            if hasLeft and hasRight:
                maxIndex = leftIndex if self.binaryHeap[leftIndex] > self.binaryHeap[rightIndex] else rightIndex;
            elif hasLeft:
                maxIndex = leftIndex;
            elif hasRight:
                maxIndex = rightIndex;

            if maxIndex != -1:
                if self.binaryHeap[maxIndex] > self.binaryHeap[index]:
                    Utility.swapUsingTempVariable(maxIndex, index, self.binaryHeap);
                    return self.heapifyDown(maxIndex);
                else:
                    return;
            else:
                return;

    def heapifyUp(self, index):
        if index <= 0:
            return;

        parentIndex = (index + 1) / 2 - 1;

        if "MIN_HEAP" is self.treeTpye:
            if self.binaryHeap[parentIndex] > self.binaryHeap[index]:
                Utility.swapUsingTempVariable(parentIndex, index, self.binaryHeap);
        elif "MAX_HEAP" is self.treeTpye:
            if self.binaryHeap[parentIndex] < self.binaryHeap[index]:
                Utility.swapUsingTempVariable(parentIndex, index, self.binaryHeap);

        return self.heapifyUp(parentIndex);

    def insert(self, data):
        self.binaryHeap.append(data);
        self.heapifyUp(len(self.binaryHeap) - 1);

    def delete(self):
        length = len(self.binaryHeap);
        if length == 0:
            return None;
        if length == 1 or length == 2:
            data = self.binaryHeap.pop(0);
            return data;
        else:
            data = self.binaryHeap[0];
            self.binaryHeap[0] = self.binaryHeap.pop();
            self.heapifyDown(0);
            return data;
    
    def findMin(self):
        if len(self.binaryHeap) == 0:
            return None;
        if "MIN_HEAP" is self.treeTpye:
            data = self.delete();
        elif "MAX_HEAP" is self.treeTpye:
            data = self.binaryHeap.pop();
        return data; 

if __name__ == '__main__':
    binaryHeapUsingArray = BinaryHeapUsingArray("MIN_HEAP");
    binaryHeapUsingArray.insert(11);
    binaryHeapUsingArray.insert(6);
    binaryHeapUsingArray.insert(8);
    binaryHeapUsingArray.insert(19);
    binaryHeapUsingArray.insert(4);
    binaryHeapUsingArray.insert(10);
    binaryHeapUsingArray.insert(5);
    binaryHeapUsingArray.insert(17);
    binaryHeapUsingArray.insert(43);
    binaryHeapUsingArray.insert(49);
    binaryHeapUsingArray.insert(31);
    
    # binaryHeapUsingArray.insert(30);
    # binaryHeapUsingArray.insert(15);
    # binaryHeapUsingArray.insert(20);
    # binaryHeapUsingArray.insert(12);
    # binaryHeapUsingArray.insert(9);
    # binaryHeapUsingArray.insert(10);
    # binaryHeapUsingArray.insert(18);
    
    binaryHeapUsingArray.traverseTree();
    
    
    print("\n");
    print(binaryHeapUsingArray.delete());
    print("Deleted");
    binaryHeapUsingArray.traverseTree();
    
#     print("\n");
#     print(binaryHeapUsingArray.delete());
#     print("Deleted");
#     binaryHeapUsingArray.traverseTree();
#     
#     print("\n");
#     print(binaryHeapUsingArray.delete());
#     print("Deleted");
#     binaryHeapUsingArray.traverseTree();
#     
#     print("\n");
#     print(binaryHeapUsingArray.delete());
#     print("Deleted");
#     binaryHeapUsingArray.traverseTree();
