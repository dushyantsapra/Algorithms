'''
Created on 21-Jun-2016

@author: Dushyant Sapra
'''

#                        _oo0oo_
#                       o8888888o
#                       88" . "88
#                       (| -_- |)
#                       0\  =  /0
#                     ___/`---'\___
#                   .' \\|     |// '.
#                  / \\|||  :  |||// \
#                 / _||||| -:- |||||- \
#                |   | \\\  -  /// |   |
#                | \_|  ''\---/''  |_/ |
#                \  .-\__  '-'  ___/-. /
#              ___'. .'  /--.--\  `. .'___
#           ."" '<  `.___\_<|>_/___.' >' "".
#          | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#          \  \ `_.   \_ __\ /__ _/   .-` /  /
#      =====`-.____`.___ \_____/___.-`___.-'=====
#                        `=---='
# 
#      ~~~~~~~~~~~~~~~~~~~~~PEACE~~~~~~~~~~~~~~~~~~~~~~


class Utility:
    @staticmethod
    def subStringCheck(mainString, subString):
        print("Checking SubString");

        iLoop = 0;
        jLoop = 0;
        length = len(mainString);
        while iLoop in range(len(subString)):
            if mainString[jLoop] is subString[iLoop]:
                iLoop += 1;
            else:
                iLoop = 0;

            if jLoop == length - 1:
                break;
            else:
                jLoop += 1;
        
        if iLoop == len(subString):
            print("Sub-String");
        else:
            print("Not a Sub-String");

    @staticmethod
    def swapUsingTempVariable(index1, index2, tempList):
        data1 = tempList[index1];
        data2 = tempList[index2];

        tempList[index1] = data2;
        tempList[index2] = data1;

    @staticmethod
    def swap(index1, index2, tempList):
        tempList[index1] = tempList[index1] + tempList[index2];
        tempList[index2] = tempList[index1] - tempList[index2];
        tempList[index1] = tempList[index1] - tempList[index2];

    @staticmethod
    def merger2SortedList(list1, list2):
        auxList = [];
        iValue = 0; jValue = 0;
        len1 = len(list1);
        len2 = len(list2);
        while iValue < len1 and jValue < len2:
            if list1[iValue] < list2[jValue]:
                auxList.append(list1[iValue]);
                iValue += 1;
            else:
                auxList.append(list2[jValue]);
                jValue += 1;

        while iValue < len1:
            auxList.append(list1[iValue]);
            iValue += 1;

        while jValue < len2:
            auxList.append(list2[jValue]);
            jValue += 1;

        print("Merged Sorted Array");
        for iValue in auxList:
            print(iValue);

        return auxList;

    @staticmethod
    def fetchGroupofN(maxsize, groupSize):
        groupList = [];

        quotient = maxsize / groupSize;

        for iLoop in range(quotient):
            groupList.append(groupSize);
            iLoop += 1;

        remainder = maxsize % groupSize;
        if (remainder) != 0:
            groupList.append(maxsize % groupSize);
        return groupList;

    @staticmethod
    def transposeOfMatrix(matrix):
        print()