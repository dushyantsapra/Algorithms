'''
Created on Oct 13, 2016

@author: Dushyant Sapra
'''
import sys

from org.ds.sortingAndSearching.Sorting import Sorting
from org.ds.utility.Utility import Utility


class ArraysQuestions:
    @staticmethod
    def findMissingNumberUsingSum(arr, numberRange):
#         Sum of n continuous numbers is n(n+1)/2

        missingNumber = (numberRange * (numberRange + 1)) / 2;

        for iLoop in range(len(arr)):
            missingNumber -= arr[iLoop];

        print("Missing Number(Using Sum Formula) is " + str(missingNumber));

    @staticmethod
    def findMissingNumberUsingXOR(arr, numberRange):
#         Let Arrays is [A1, A2, A3, A5] so A4 is and 
#         Below Logic would be [A1, A2, A3, A5] ^ [A1, A2, A3, A4, A5] = [A1 ^ A1] ^ [A2 ^ A2] ^ [A3 ^ A3] ^ [A4] ^ [A5 ^ A5]
#         Since XOR of Same Number is 0 and XOR of O with any number would be the number itself, so Result would be A4

        actualSum = 0;
        currentSum = 0;

        for iLoop in range(1, numberRange + 1):
            actualSum = iLoop ^ actualSum;

        for iLoop in range(len(arr)):
            currentSum = arr[iLoop] ^ currentSum;

        missingNumber = currentSum ^ actualSum;

        print("Missing Number(Using XOR) is " + str(missingNumber));

    @staticmethod
    def moveAllElementExceptGivenAtBackOfArray(arr, element):
        iLoop = len(arr) - 1;
        jLoop = len(arr) - 1;

        while iLoop >= 0:
            if arr[iLoop] != element:
                if iLoop != jLoop:
                    Utility.swapUsingTempVariable(iLoop, jLoop, arr);
                jLoop -= 1;
            iLoop -= 1;          

    @staticmethod
    def mergeTwoSortedArray(arr1, arr2):
#         Here First Array can store element of Array2 Also
#         Both the Arrays are sorted
#         Array1 Contains -1 Element for empty Space, These -1 would be replaced with element of Array2
        ArraysQuestions.moveAllElementExceptGivenAtBackOfArray(arr1, -1);

        maxLength = len(arr1);
        minLength = len(arr2);

        jLoop = minLength;
        kLoop = 0;

        for iLoop in range(maxLength):
            if jLoop < (maxLength) and arr1[jLoop] < arr2[kLoop]:
                Utility.swapUsingTempVariable(iLoop, jLoop, arr1);
                jLoop += 1;
            else:
                arr1[iLoop] = arr2[kLoop];
                kLoop += 1;

        print("Merged Array is " + str(arr1));
    
    @staticmethod
    def findNumberOccuringOddNumberOfTimes(arr):
        number = 0;
        for element in arr:
            number ^= element;

        print("Number Occuring Odd Number Of Times is " + str(number));

    @staticmethod
    def segregateOand1InArray(arr):
        iLoop = 0;
        jLoop = len(arr) - 1;

        while iLoop < jLoop:
            if arr[iLoop] == 0:
                iLoop += 1;

            if arr[jLoop] == 1:
                jLoop -= 1;
            
            if not arr[iLoop] == 0 and not arr[jLoop] == 1:
                Utility.swapUsingTempVariable(iLoop, jLoop, arr);

        print("\nSegregated Array is " + str(arr));

    @staticmethod
    def findMinAndMaxOfArray(arr):
        minimum = arr[0];
        maximum = arr[0];

        for iLoop in range(1, len(arr)):
            if arr[iLoop] < minimum:
                minimum = arr[iLoop];
            elif arr[iLoop] > maximum:
                maximum = arr[iLoop];

        print("\nMin of Array is " + str(minimum) + ", Max of Array is " + str(maximum));

    @staticmethod
    def findMinAndMaxOfArrayUsingTournamentMethodHelper(arr, sIndex, eIndex):
        if sIndex == eIndex:
            return arr[sIndex], arr[eIndex];
        elif eIndex - sIndex == 1:
            minimum, maximun = (arr[sIndex], arr[eIndex]) if arr[sIndex] < arr[eIndex] else (arr[eIndex], arr[sIndex]);
            return minimum, maximun;
        else:
            min1, max1 = ArraysQuestions.findMinAndMaxOfArrayUsingTournamentMethodHelper(arr, sIndex, (eIndex + sIndex - 1) / 2);
            min2, max2 = ArraysQuestions.findMinAndMaxOfArrayUsingTournamentMethodHelper(arr, ((eIndex + sIndex - 1) / 2) + 1, eIndex);

            minimum = min1 if min1 < min2 else min2;
            maximum = max1 if max1 > max2 else max2;
            return minimum, maximum;

    @staticmethod
    def findMinAndMaxOfArrayUsingTournamentMethod(arr):
        minimum, maximum = ArraysQuestions.findMinAndMaxOfArrayUsingTournamentMethodHelper(arr, 0, len(arr) - 1);

        print("\n(Tournament Method)Min of Array is " + str(minimum) + ", Max of Array is " + str(maximum));
    
    @staticmethod
    def findMaxDiffBwTwoNumberOfArray(arr):
#         Maximum difference between two elements such that larger element appears after the smaller number
        if len(arr) < 2:
            print("\nGiven Array Size is Less Then 2");
            return

        minimum, maximum = (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0]);

        diff = maximum - minimum;

        for iLoop in range(2, len(arr)):
            if arr[iLoop] < minimum:
                minimum = arr[iLoop];
            elif arr[iLoop] > maximum:
                maximum = arr[iLoop]
                diff = maximum - minimum;

        print("\nMax Diff is " + str(diff));

    @staticmethod
    def findUnionAndIntersectionofTwoSortedArray(arr1, arr2):
        minLength, maxLength, minArr, maxArr = (len(arr1), len(arr2), arr1, arr2) if len(arr1) < len(arr2) else (len(arr2), len(arr1), arr2, arr1);

        unionArr = [];
        intersectionArr = [];

        iLoop = 0;
        jLoop = 0;

        while iLoop < maxLength:
            if minArr[jLoop] == maxArr[iLoop]:
                intersectionArr.append(maxArr[iLoop]);
                unionArr.append(maxArr[iLoop])
                iLoop += 1;
                jLoop += 1;
            elif minArr[jLoop] < maxArr[iLoop]:
                unionArr.append(minArr[jLoop])
                jLoop += 1;
            else:
                unionArr.append(maxArr[iLoop])
                iLoop += 1;

            if jLoop == minLength:
                break;

        while iLoop < maxLength:
            unionArr.append(maxArr[iLoop])
            iLoop += 1;
            
        while jLoop < minLength:
            unionArr.append(minArr[jLoop])
            jLoop += 1;

        print("\nUnion Array is " + str(unionArr) + ", Intersection Array is " + str(intersectionArr));

    @staticmethod
    def findFloorAndCeilingOfANumberInSortedArray(arr, number):
#         Given a sorted array and a value x, the ceiling of x is the smallest element in array greater than or equal to x, and the floor is the greatest element smaller than or equal to x. Assume than the array is sorted in non-decreasing orde
        print();

    @staticmethod
    def productArrayPuzzle(arr):
#         Given an array arr[] of n integers, construct a Product Array prod[] (of same size) such that prod[i] is equal to the product of all the elements of arr[] except arr[i]
        length = len(arr);
        leftProduct = [0] * length;
        rightProduct = [0] * length;
        product = [0] * length;

        leftProduct[0] = arr[0];
        for iLoop in range(1, length):
            leftProduct[iLoop] = leftProduct[iLoop - 1] * arr[iLoop];

        rightProduct[length - 1] = arr[length - 1];
        for iLoop in reversed(range(length - 1)):
            rightProduct[iLoop] = rightProduct[iLoop + 1] * arr[iLoop];

        product[0] = rightProduct[1];
        product[length - 1] = leftProduct[length - 2];
        for iLoop in range(1, length - 1):
            product[iLoop] = leftProduct[iLoop - 1] * rightProduct[iLoop + 1];

        print("\nProduct Array is " + str(product));
    
    @staticmethod
    def printLeaders(arr):
        leaders = [];

        length = len(arr);

        currentLeader = arr[length - 1]
        leaders.append(currentLeader);

        for iLoop in reversed(range(length - 1)):
            if arr[iLoop] > currentLeader:
                leaders.append(arr[iLoop]);
                currentLeader = arr[iLoop];

        print("\nLeaders in an Array are " + str(leaders));

    @staticmethod
    def contiguousSubArrayWithLargestSum(arr):
        length = len(arr);

        maxSum = arr[0];
        curSum = arr[0];

        for iLoop in range(1, length):
            curSum = max(arr[iLoop], curSum + arr[iLoop]);
            maxSum = max(curSum, maxSum);

        print("contiguousSubArrayWithLargestSum is " + str(maxSum));

    @staticmethod
    def findPairWithGivenSumInUnsortedArrayUsingSorting(arr, maxSum):
        Sorting.mergeSort(arr, False);

        iLoop = 0;
        jLoop = len(arr) - 1;

        isFound = False;

        while iLoop < jLoop:
            if maxSum == (arr[iLoop] + arr[jLoop]):
                isFound = True;
                break;
            elif maxSum < (arr[iLoop] + arr[jLoop]):
                jLoop -= 1;
            else:
                iLoop += 1;

        if isFound:
            print("Largest Pair Sum Formed by " + str(arr[iLoop]) + " and " + str(arr[jLoop]));
        else:
            print("Pair With Given Sum doesn't Exists");

    @staticmethod
    def findPairWithGivenSumInUnsortedArrayUsingHashing(arr, maxSum):
        hashMap = {};

        length = len(arr);

        for iLoop in range(length):
            tempValue = maxSum - arr[iLoop];
            if tempValue in hashMap:
                print("Largest Pair Sum Formed by " + str(arr[iLoop]) + " and " + str(tempValue));
                return;

            hashMap[arr[iLoop]] = True;

        print("Pair With Given Sum doesn't Exists");

    @staticmethod
    def findPairWithGivenSumInUnsortedArray(arr, maxSum):
#         ArraysQuestions.findPairWithGivenSumInUnsortedArrayUsingSorting(arr, maxSum);
        ArraysQuestions.findPairWithGivenSumInUnsortedArrayUsingHashing(arr, maxSum);
    
    @staticmethod
    def findSubArrayWithGivenSumInNonNegativeArray(arr, maxSum):
        currentSum = 0;

        sIndex = 0;

        length = len(arr);
        
        isFound = False;

        for iLoop in range(length):
            while (maxSum < currentSum + arr[iLoop]) and sIndex < iLoop:
                currentSum -= arr[sIndex];
                sIndex += 1;

            currentSum += arr[iLoop];
            
            if maxSum == currentSum:
                isFound = True;
                break;

        if isFound:
            print("Max Sum Exists B/w Index " + str(sIndex) + " To Index " + str(iLoop));
        else:
            print("Doesn't Exists")
    
    @staticmethod
    def findSmallestAndSecondSmallestNumberInArra(arr):
        smallest = sys.maxint;
        secondSmallest = sys.maxint;

        length = len(arr);

        for iLoop in range(length):
            if smallest > arr[iLoop]:
                secondSmallest = smallest;
                smallest = arr[iLoop];
            elif secondSmallest > arr[iLoop]:
                secondSmallest = arr[iLoop];

        print("Smallest is " + str(smallest) + ", Second Smallest is " + str(secondSmallest));

    @staticmethod
    def sortArrayInWaveFormUsingSorting(arr):
        Sorting.mergeSort(arr, False);

        length = len(arr);

        iLoop = 0;

        while iLoop < length - 1:
            Utility.swapUsingTempVariable(iLoop, iLoop + 1, arr);
            iLoop += 2;
        
        print("sortArrayInWaveFormUsingSorting " + str(arr));

    @staticmethod
    def sortArrayInWaveFormSingleIteration(arr):
        if arr[0] < arr[1]:
            Utility.swapUsingTempVariable(0, 1, arr);
        
        length = len(arr);
        
        iLoop = 3;
        
        while iLoop < length:
            if arr[iLoop] < arr[iLoop - 1]:
                Utility.swapUsingTempVariable(iLoop, iLoop - 1, arr);
            
            iLoop += 2;
        
        print("sortArrayInWaveFormSingleIteration " + str(arr));
    
    @staticmethod
    def sortArrayInWaveForm(arr):
#         ArraysQuestions.sortArrayInWaveFormUsingSorting(arr);
        ArraysQuestions.sortArrayInWaveFormSingleIteration(arr);

if __name__ == '__main__':
    ArraysQuestions.findMissingNumberUsingXOR([1, 3, 4, 5], 5);

    ArraysQuestions.findMissingNumberUsingSum([1, 3, 4, 5], 5);

    ArraysQuestions.mergeTwoSortedArray([2, 8, -1, -1, -1, 13, -1, 15, 20], [5, 7, 9, 25]);

    ArraysQuestions.findNumberOccuringOddNumberOfTimes([1, 2, 3, 1, 2, 3, 3]);

    ArraysQuestions.segregateOand1InArray([0, 1, 0, 1, 0, 0, 1, 1, 1, 0]);

    ArraysQuestions.findMinAndMaxOfArray([-1000, 11, 445, 1, 330, -3000]);

    ArraysQuestions.findMinAndMaxOfArrayUsingTournamentMethod([-1000, 11, 445, 1, 330, -3000]);
    
    ArraysQuestions.findMaxDiffBwTwoNumberOfArray([3, 12, 2, 4, 15, 1]);
    
    ArraysQuestions.findUnionAndIntersectionofTwoSortedArray([1, 3, 5, 7, 8, 9], [2, 3, 5, 7, 8 , 9, 10]);
    
    ArraysQuestions.productArrayPuzzle([10, 3, 5, 6, 2]);
    
    ArraysQuestions.printLeaders([16, 17, 4, 3, 5, 2]);
    
    ArraysQuestions.contiguousSubArrayWithLargestSum([-2, -3, 4, -1, -2, 1, 5, -3]);
    ArraysQuestions.contiguousSubArrayWithLargestSum([-2, -3, -4, -1, -2, -5, -3]);
    
    ArraysQuestions.findPairWithGivenSumInUnsortedArray([-2, -3, 4, -1, -2, -1, 5, -3], 5)
    
    ArraysQuestions.findSubArrayWithGivenSumInNonNegativeArray([15, 2, 4, 8, 9, 5, 10, 23], 23);
    
    ArraysQuestions.findSmallestAndSecondSmallestNumberInArra([15, 2, 4, 8, 9, 5, 10, 23]);
    
    ArraysQuestions.sortArrayInWaveForm([10, 90, 49, 2, 1, 5, 23]);
    
#     print(1 ^ 9 ^ 8 ^ 8 ^ 7 ^ 6 ^ 4 ^ 3 ^ 2 ^ 5 ^ 5);
#     print(1 ^ 9 ^ 8 ^ 7 ^ 6 ^ 4 ^ 3 ^ 2 ^ 5);    
