'''
Created on Nov 1, 2016

@author: Dushyant Sapra
'''

class KMPAlgo:
    @staticmethod
    def computeSuffixWhichIsPrefixOfGivenString(string):
        stringLength = len(string);
        suffixPrefixArray = [0] * stringLength;

        if stringLength == 1:
            return suffixPrefixArray;

        iLoop = 0;
        jLoop = 1;
        while jLoop < stringLength:
            if string[iLoop] == string[jLoop]:
                suffixPrefixArray[jLoop] = iLoop + 1;
                iLoop += 1;
                jLoop += 1;
            else:
                if iLoop == 0:
                    suffixPrefixArray[jLoop] = 0;
                    jLoop += 1;
                else:
                    iLoop = suffixPrefixArray[iLoop - 1];
        return suffixPrefixArray;

    @staticmethod
    def kmpAlgo(mainString, subString):
        suffixPrefixArray = KMPAlgo.computeSuffixWhichIsPrefixOfGivenString(subString);

        iLoop = 0;
        jLoop = 0;

        mainStringLength = len(mainString);
        subStringLength = len(subString);

        while iLoop < mainStringLength and jLoop < subStringLength:
            if mainString[iLoop] == subString[jLoop]:
                iLoop += 1;
                jLoop += 1;
            else:
                if jLoop == 0:
                    iLoop += 1;
                else:
                    jLoop = suffixPrefixArray[jLoop - 1];

        if jLoop == len(subString):
            print("Given String is SubString of main String");
        else:
            print("Given String is not SubString of main String");

if __name__ == '__main__':
    KMPAlgo.kmpAlgo("abcxabcdabxabcabcdabcy", "abcdabv");
    KMPAlgo.kmpAlgo("THIS IS A TEST TEXT", "TEST");
    KMPAlgo.kmpAlgo("AABAACAADAABAAABAA", "AABA");
    KMPAlgo.kmpAlgo("ABABABCABABABCABABABC", "ABABAC");
    KMPAlgo.kmpAlgo("ABABDABACDABABCABAB", "ABABCABAB");
    KMPAlgo.kmpAlgo("13213013201", "1320")
    
    
    
    
