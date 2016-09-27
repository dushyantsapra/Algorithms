'''
Created on Jul 27, 2016

@author: Dushyant Sapra
'''

class FenwickOrBinaryIndexedTree:
    def __init__(self):
        self.originalArray = [];
        self.fenwickArray = [];

    def getTwosComplement(self, data):
        return (~int(data)) + 1;

    def getNext(self, index):
        return index + (index & -index);

    def getParent(self, index):
        return index - (index & -index);

#     Here ithElement is not index of Array, index would be ithElement - 1.
#     i.e if ithElement is 5 then we would return sum from index 0 to 4
    def getSumHelper(self, index):

        tempSum = self.fenwickArray[index];
        parentIndex = self.getParent(index);
        if parentIndex > 0:
            tempSum += self.getSumHelper(parentIndex);

        return tempSum;

#     if startIndex starts from 0, then getSum by calling getSumHelper function with endIndex + 1, as fenwickArray size is 1 greater then actual array
#     if startIndex starts with valus greater then 0, then for range (l, r) call getSumHelper(r+1) - getSumHelper(l)
    def getSum(self, startIndex, endIndex):
#         As Size of fenwickArray would be 1 greater then actual array
        if endIndex > len(self.fenwickArray) - 2:
            return 0;
        if startIndex == 0:
            return self.getSumHelper(endIndex + 1);
        else:
            return self.getSumHelper(endIndex + 1) - self.getSumHelper(startIndex);

    def updateFenWickTreeHelper(self, index, diff):
        self.fenwickArray[index] = self.fenwickArray[index] + diff;
        nextIndex = self.getNext(index);
        if nextIndex > len(self.fenwickArray) - 2:
            return True;
        
        return self.updateFenWickTreeHelper(nextIndex, diff);

    def updateFenwickTree(self, index, newElement):
        if index > len(self.originalArray):
            return False;
        else:
            if (newElement - self.originalArray[index]) == 0:
                return True;
            self.updateFenWickTreeHelper((index + 1), (newElement - self.originalArray[index]));

    def createFenwickTreeHelper(self, inputArray, currentIndex, fenwinkArrayIndex):
        self.fenwickArray[fenwinkArrayIndex] += inputArray[currentIndex];
        fenwinkArrayIndex = self.getNext(fenwinkArrayIndex);
        if fenwinkArrayIndex >= (len(self.fenwickArray)):
            return;

        return self.createFenwickTreeHelper(inputArray, currentIndex, fenwinkArrayIndex);

    def createFenwickTree(self, inputArray):
        self.originalArray = inputArray;
        self.fenwickArray = [0] * (len(self.originalArray) + 1);
        for iValue in range(len(self.originalArray)):
            self.createFenwickTreeHelper(self.originalArray, iValue, (iValue + 1));

tree = FenwickOrBinaryIndexedTree();
tempArray = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3];
tree.createFenwickTree(tempArray);

for iValue in range(len(tree.fenwickArray)):
    print (tree.fenwickArray[iValue]);

print("Sum is %d", tree.getSum(2, 11));

tree.updateFenwickTree(5, 8);
for iValue in range(len(tree.fenwickArray)):
    print (tree.fenwickArray[iValue]);