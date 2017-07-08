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
    def swapUsingXOR(index1, index2, tempList):
        tempList[index1] = tempList[index1] ^ tempList[index2];
        tempList[index2] = tempList[index1] ^ tempList[index2];
        tempList[index1] = tempList[index1] ^ tempList[index2];

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

    @staticmethod
    def gcdUsingSubtraction(num1, num2):
        while num1 != num2:
            if num1 > num2 - 1:
                num1 = num1 - num2;
            else:
                num2 = num2 - num1;

        print("GCD(Using Substraction) is " + str(num1));

    @staticmethod
    def gcdUsingModulus(num1, num2):
        minimum = num1 if num1 < num2 else num2;

        while minimum > 0 :
            if num1 % minimum == 0 and num2 % minimum == 0:
                break;
        
            minimum -= 1;

        print("GCD(Using Modulus) is " + str(minimum));
    
    @staticmethod
    def multiplication(multiplier, final_array, current_array_size):
        carry_forward = 0
        for index in range(current_array_size):
            prod = int(int(final_array[index] * multiplier) + carry_forward);
            final_array[index] = int(prod % 10);
            carry_forward = int(prod / 10);
        
        while carry_forward > 0:
            final_array[current_array_size] = int(carry_forward % 10);
            carry_forward = int(carry_forward / 10);
            current_array_size += 1;
        
        return current_array_size;
    
    @staticmethod
    def factorial(number):
        MAX_SIZE = 500;
        
        final_array = [1 for _ in range(MAX_SIZE)];
    
        current_array_size = 1;
        
        for multiplier in range(2, number + 1):
            current_array_size = Utility.multiplication(multiplier, final_array, current_array_size);
        
        string_array = [];
        for index in reversed(range(current_array_size)):
            string_array.append(str(final_array[index]));
        
        print(''.join(string_array))
        return ''.join(string_array);
    
    @staticmethod
    def compute_combination(n, r):
        print()

if __name__ == '__main__':
#     Utility.gcdUsingSubtraction(5, 7);
#     Utility.gcdUsingModulus(4, 8);
#     Utility.mergeTwoSortedArray([1, 5, -1, -1, 20, -1, 35], [2, 11, 25]);

    Utility.factorial(25)
