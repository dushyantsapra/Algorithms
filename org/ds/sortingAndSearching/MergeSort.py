'''
@author: Dushyant Sapra
'''

class MergeSort:
    def mergeHelper(self, sIndex, midIndex, eIndex, orgList):
        tempList = [];
#         midIndex = int((sIndex + eIndex) / 2);
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

    def mergeSortHelper(self, startIndex, endIndex, tempList):
#         if endIndex - startIndex == 1:
#             if tempList[startIndex] > tempList[endIndex]:
#                 Utility.swap(startIndex, endIndex, tempList);
#             return;

        if startIndex < endIndex:
            midIndex = int ((startIndex + endIndex) / 2);
    
            self.mergeSortHelper(startIndex, midIndex, tempList);
            self.mergeSortHelper(midIndex + 1, endIndex, tempList);
            self.mergeHelper(startIndex, midIndex, endIndex, tempList);

        return None;

    def mergeSort(self, tempList):
        self.mergeSortHelper(0, len(tempList) - 1, tempList);

        print("Merge Sort");
        for iValue in tempList:
            print(iValue);

if __name__ == '__main__': 
    tempList = [6, 5, 3, 1, 8, 7, 2, 4];
    sort = MergeSort();
    sort.mergeSort(tempList);
