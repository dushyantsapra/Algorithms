
class Sorting:
    @staticmethod
    def insertionSort(tempList):
        tempValue = 0
        for iValue in range(len(tempList)):
            tempValue = iValue
            for jValue in reversed(range(iValue)):
                if tempList[tempValue] < tempList[jValue]:
                    tempList[tempValue], tempList[jValue] = tempList[jValue], tempList[tempValue]
                    tempValue = jValue

        print("Insertion Sort")

        for iValue in tempList:
            print(iValue, end=" ")
        print()

    # Select Smallest Number on Every Iteration.
    @staticmethod
    def selectionSort(tempList):
        minIndex = 0;
        listLen = len(tempList);
        for iValue in range(listLen):
            minIndex = iValue;
            for jValue in range(iValue, listLen):
                if tempList[minIndex] > tempList[jValue]:
                    minIndex = jValue;
            if minIndex != iValue:
                tempList[minIndex], tempList[iValue] = tempList[iValue], tempList[minIndex]

        print("Selection Sort");
        for iValue in tempList:
            print(iValue, end=" ");
        print()

    # Compare Adjacent Pairs
    @staticmethod
    def bubbleSort(tempList):
        listLen = len(tempList)
        for iValue in range(listLen):
            for jValue in range(listLen - 1 - iValue):
                if(tempList[jValue] > tempList[jValue + 1]):
                    tempList[jValue], tempList[jValue + 1] = tempList[jValue + 1], tempList[jValue]

        print("Bubble Sort")
        for iValue in tempList:
            print(iValue, end=" ")
        print()

    @staticmethod
    def mergeHelper(sIndex, midIndex, eIndex, orgList):
        tempList = [];
        iValue = sIndex;
        jValue = midIndex + 1;

        while iValue <= midIndex and jValue < eIndex + 1:
            if orgList[iValue] < orgList[jValue]:
                tempList.append(orgList[iValue]);
                iValue += 1;
            else:
                tempList.append(orgList[jValue]);
                jValue += 1;

        while iValue <= midIndex:
            tempList.append(orgList[iValue]);
            iValue += 1;

        while jValue < eIndex + 1:
            tempList.append(orgList[jValue]);
            jValue += 1;

        iIndex = sIndex;
        for value in tempList:
            orgList[iIndex] = value;
            iIndex += 1;

        return None;

    @staticmethod
    def mergeSortHelper(startIndex, endIndex, tempList):
        if startIndex < endIndex:
            midIndex = int ((startIndex + endIndex) / 2);
    
            Sorting.mergeSortHelper(startIndex, midIndex, tempList);
            Sorting.mergeSortHelper(midIndex + 1, endIndex, tempList);
            Sorting.mergeHelper(startIndex, midIndex, endIndex, tempList);

        return None;

    @staticmethod
    def mergeSort(tempList, isPrint=True):
        Sorting.mergeSortHelper(0, len(tempList) - 1, tempList);

        if isPrint:
            print("Merge Sort");
            for iValue in tempList:
                print(iValue, end=" ");
        print()
    
    @staticmethod
    def quickSortPartition(sIndex, eIndex, orgList):
        pivot = orgList[eIndex];
        iValue = sIndex - 1;
        for jValue in range(sIndex, eIndex):
            if orgList[jValue] <= pivot:
                iValue += 1;
                orgList[iValue], orgList[jValue] = orgList[jValue], orgList[iValue] 
        iValue += 1;
        orgList[iValue], orgList[eIndex] = orgList[eIndex], orgList[iValue]
        print(orgList)
        return iValue;

    @staticmethod
    def quickSortHelper(sIndex, eIndex, orgList):
        if(sIndex < eIndex):
            pivotIndex = Sorting.quickSortPartition(sIndex, eIndex, orgList);
            Sorting.quickSortHelper(sIndex, pivotIndex - 1, orgList);
            Sorting.quickSortHelper(pivotIndex + 1, eIndex, orgList);

    @staticmethod
    def quickSort(tempList):
        Sorting.quickSortHelper(0, len(tempList) - 1, tempList);

        print("Quick Sort");
        for value in tempList:
            print(value, end=" ");
        print()
    
if __name__ == '__main__':
    Sorting.insertionSort([6, 5, 3, 1, 8, 7, 2, 4]);
    Sorting.selectionSort([6, 5, 3, 1, 8, 7, 2, 4]);
    Sorting.bubbleSort([6, 5, 3, 1, 8, 7, 2, 4]);
    Sorting.mergeSort([6, 5, 3, 1, 8, 7, 2, 4]);
    Sorting.quickSort([1, 2, 3, 4, 5])
    Sorting.quickSort([6, 5, 3, 1, 8, 7, 2, 4])
    Sorting.quickSort([1, 3, 9, 8, 2, 7, 5])

