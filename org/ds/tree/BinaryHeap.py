'''
Created on 17-Jun-2016

@author: Dushyant Sapra
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

class BinaryHeapNode:
    def __init__(self, data, priority):
        self.data = data;
        self.priority = priority;
        
    def getData(self):
        return self.data;
    
    def setPriority(self, newPriority):
        self.priority = newPriority;
    
    def getPriority(self):
        return self.priority;

    def __str__(self):
        return "Data is " + self.data + ", And Priority is " + str(self.priority); 

class BinaryHeapUsingArray:
    def __init__(self, treeType):
        self.treeTpye = treeType;
#         Will Store Binary Heap Node
        self.binaryHeap = [];
#         Will Store Actual Data with its binary heap Node index in binaryHeap array/List
        self.binaryNodePositionMap = {};

    def getHeap(self):
        return self.binaryHeap;

    def traverseTree(self):
        for value in self.binaryHeap:
            print(value);

    def getHeapSize(self):
        return len(self.binaryHeap);
    
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
                minIndex = leftIndex if self.binaryHeap[leftIndex].getPriority() < self.binaryHeap[rightIndex].getPriority() else rightIndex;
            elif hasLeft:
                minIndex = leftIndex;
            elif hasRight:
                minIndex = rightIndex;

            if minIndex != -1:
                if self.binaryHeap[minIndex].getPriority() < self.binaryHeap[index].getPriority():
                    self.binaryNodePositionMap[self.binaryHeap[index].getData()] = minIndex;
                    self.binaryNodePositionMap[self.binaryHeap[minIndex].getData()] = index;
                    Utility.swapUsingTempVariable(minIndex, index, self.binaryHeap);
                    return  self.heapifyDown(minIndex);
                else:
                    return;
            else:
                return;
        elif "MAX_HEAP" is self.treeTpye:
            if hasLeft and hasRight:
                maxIndex = leftIndex if self.binaryHeap[leftIndex].getPriority() > self.binaryHeap[rightIndex].getPriority() else rightIndex;
            elif hasLeft:
                maxIndex = leftIndex;
            elif hasRight:
                maxIndex = rightIndex;

            if maxIndex != -1:
                if self.binaryHeap[maxIndex].getPriority() > self.binaryHeap[index].getPriority():
                    self.binaryNodePositionMap[self.binaryHeap[index].getData()] = maxIndex;
                    self.binaryNodePositionMap[self.binaryHeap[maxIndex].getData()] = index;
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
            if self.binaryHeap[parentIndex].getPriority() > self.binaryHeap[index].getPriority():
                self.binaryNodePositionMap[self.binaryHeap[index].getData()] = parentIndex;
                self.binaryNodePositionMap[self.binaryHeap[parentIndex].getData()] = index;
                Utility.swapUsingTempVariable(parentIndex, index, self.binaryHeap);
        elif "MAX_HEAP" is self.treeTpye:
            if self.binaryHeap[parentIndex].getPriority() < self.binaryHeap[index].getPriority():
                self.binaryNodePositionMap[self.binaryHeap[index].getData()] = parentIndex;
                self.binaryNodePositionMap[self.binaryHeap[parentIndex].getData()] = index;
                Utility.swapUsingTempVariable(parentIndex, index, self.binaryHeap);

        return self.heapifyUp(parentIndex);

    def insert(self, data, priority):
        node = BinaryHeapNode(data, priority);
        self.binaryHeap.append(node);
        index = len(self.binaryHeap) - 1;
        self.binaryNodePositionMap[data] = index;
        self.heapifyUp(len(self.binaryHeap) - 1);

    def findMin(self):
        length = len(self.binaryHeap);
        if length == 0:
            return None;
        if length == 1 or length == 2:
            node = self.binaryHeap.pop(0);
            del self.binaryNodePositionMap[node.getData()];
            if len(self.binaryHeap) == 1:
                self.binaryNodePositionMap[self.binaryNodePositionMap.keys()[0]] = 0;
            return node.getData();
        else:
            node = self.binaryHeap[0];
            del self.binaryNodePositionMap[node.getData()];
            self.binaryHeap[0] = self.binaryHeap.pop();
            self.heapifyDown(0);
            return node.getData();

    def delete(self, data):
        if data not in self.binaryNodePositionMap:
            print("Data Given is not Present in Binary Heap");
            return None;

        index = self.binaryNodePositionMap[data];

        length = len(self.binaryHeap);
        if length == 1 or length == 2:
            node = self.binaryHeap.pop(index);
            del self.binaryNodePositionMap[node.getData()];
            if len(self.binaryHeap) == 1:
                self.binaryNodePositionMap[self.binaryNodePositionMap.keys()[0]] = 0;
            return node.getData();
        elif index == length - 1:
            node = self.binaryHeap.pop();
            del self.binaryNodePositionMap[node.getData()];
            return node.getData();
        else:
            del self.binaryNodePositionMap[self.binaryHeap[index].getData()];
            self.binaryHeap[index] = self.binaryHeap.pop();
            self.heapifyDown(index);

#     HeapifyUp
    def decreasePriority(self, data, newPriority):
        if data not in self.binaryNodePositionMap:
            return False;
        index = self.binaryNodePositionMap[data];
        node = self.binaryHeap[self.binaryNodePositionMap[data]];
        
        if node.getPriority() > newPriority:
            node.setPriority(newPriority);
            self.heapifyUp(index);
            return True;
        else:
            return False;

#     HeapifyDown
    def increasePriority(self, data, newPriority):
        if data not in self.binaryNodePositionMap:
            return False;
        index = self.binaryNodePositionMap[data];
        node = self.binaryHeap[self.binaryNodePositionMap[data]];

        if node.getPriority() < newPriority:
            node.setPriority(newPriority);
            self.heapifyDown(index);
        else:
            return False;

    def changePriority(self, data, newPriority):
        if data not in self.binaryNodePositionMap:
            print("Data Given is not Present in Binary Heap");
            return False;
        currentPriority = self.binaryHeap[self.binaryNodePositionMap[data]].getPriority();
        if currentPriority == newPriority:
            print("New and Current Priority are same");
            return False;
        elif  currentPriority > newPriority:
            self.decreasePriority(data, newPriority);
        else:
            self.increasePriority(data, newPriority);
        return True;

if __name__ == '__main__':
    binaryHeapUsingArray = BinaryHeapUsingArray("MIN_HEAP");
    binaryHeapUsingArray.insert("E1", 8);
    binaryHeapUsingArray.insert("E2", 4);
    binaryHeapUsingArray.insert("E3", 3);
    binaryHeapUsingArray.insert("E4", 10);
    binaryHeapUsingArray.insert("E5", 5);
    
    binaryHeapUsingArray.traverseTree();
    
    """print(binaryHeapUsingArray.findMin());
    print("Traversing Again");
    binaryHeapUsingArray.traverseTree();"""
    
    """binaryHeapUsingArray.changePriority("E5", 11);
    print("Traversing Again");
    binaryHeapUsingArray.traverseTree();"""
    
    binaryHeapUsingArray.delete("E3");
    print("Traversing Again");
    binaryHeapUsingArray.traverseTree();
