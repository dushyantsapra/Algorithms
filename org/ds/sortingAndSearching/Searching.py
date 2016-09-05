'''
Created on 28-Jun-2016

@author: Dushyant Sapra
'''

class Searching:
    def __init__(self, tempArray):
        self.tempArray = tempArray;

    def binarySearch(self, toSearch, sIndex, eIndex):
        mid = -1;
        if eIndex >= sIndex:
            mid = sIndex + (eIndex - sIndex) / 2;

            if self.tempArray[mid] == toSearch:
                return True;
            elif self.tempArray[mid] > toSearch:
                return self.binarySearch(toSearch, sIndex, mid);
            elif self.tempArray[mid] < toSearch:
                return self.binarySearch(toSearch, mid + 1, eIndex);
        else:
            return False;

    def linearSearch(self, toSearch):
        for num in self.tempArray:
            if num is toSearch:
                return True;
        return False;

tempArray = [10, 6, 5, 12, 57];
linearSearch = Searching(tempArray);
result = linearSearch.linearSearch(15);

tempArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11];
binarySearch = Searching(tempArray);
result = binarySearch.binarySearch(11, 0, len(tempArray) - 1);
print(result);
