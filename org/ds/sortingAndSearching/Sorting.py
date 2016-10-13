from org.ds.utility.Utility import Utility

class Sorting:
    def insertionSort(self, tempList):
        tempValue = 0;
        for iValue in range(len(tempList)):
            tempValue = iValue;
            for jValue in reversed(range(iValue)):
                if tempList[tempValue] < tempList[jValue]:
                    Utility.swap(tempValue, jValue, tempList);
                    tempValue = jValue;

        print("Insertion Sort");
        for iValue in tempList:
            print(iValue);

# Select Smallest Number on Every Iteration.
    def selectionSort(self, tempList):
        minIndex = 0;
        listLen = len(tempList);
        for iValue in range(listLen):
            minIndex = iValue;
            for jValue in range(iValue, listLen):
                if tempList[minIndex] > tempList[jValue]:
                    minIndex = jValue;
            if minIndex != iValue:
                Utility.swap(minIndex, iValue, tempList);

        print("Selection Sort");
        for iValue in tempList:
            print(iValue);

# Compare Adjacent Pairs
    def bubbleSort(self, tempList):
        listLen = len(tempList);
        for iValue in range(listLen):
            for jValue in range(listLen - 1 - iValue):
                if(tempList[jValue] > tempList[jValue + 1]):
                    Utility.swap(jValue, jValue + 1, tempList);

        print("Bubble Sort");
        for iValue in tempList:
            print(iValue);

    def test(self):
        for jValue in range(1, 6):
            print(jValue);

tempList = [6, 5, 3, 1, 8, 7, 2, 4];
sort = Sorting();
sort.insertionSort(tempList);
sort.selectionSort(tempList);
sort.bubbleSort(tempList);
