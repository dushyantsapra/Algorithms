'''
Created on Oct 12, 2016

@author: Dushyant Sapra
'''

class HashingUtility:
#     Check if a given array contains duplicate elements within k distance from each other
    @staticmethod
    def checkForDupicateWithInKDistanceInArray(arr, k):
        hashMap = {};

        lenght = len(arr);

        isDuplicate = False;
        iLoop = 0;

        for iLoop in range(lenght):
            if arr[iLoop] in hashMap:
                isDuplicate = True;
                break;

            hashMap[arr[iLoop]] = True;

            if iLoop > k:
                del hashMap[arr[iLoop - k]];

        if isDuplicate:
            print("\nValue " + str(arr[iLoop]) + " has a Duplicate");
        else:
            print("\nNo Duplicate Present");

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5];

    HashingUtility.checkForDupicateWithInKDistanceInArray(arr, 3);
