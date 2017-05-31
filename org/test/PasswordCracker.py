'''
Created on May 30, 2017

@author: sapra
'''

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

def kmpAlgo(mainString, subString, suffixPrefixArray):
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
        return True, iLoop
    else:
        return False, iLoop

if __name__ == '__main__':
    inputfile = open("/home/sapra/input.txt");
    test_count = int(inputfile.readline().strip())
    for _ in range(test_count):
        pwd_count = int(inputfile.readline().strip())
        pwd_list = list(inputfile.readline().strip().split(" "))
        loginAttempt = inputfile.readline().strip()
    
        login_attempt_len = len(loginAttempt)
    
        suffixPrefixArrayList = []
        for pwd in pwd_list:
            suffixPrefixArrayList.append(computeSuffixWhichIsPrefixOfGivenString(pwd))
        
        current_count = 0
        iLoop = 0
        index = 0
        current_len = login_attempt_len
        previous_index = 0
        found_string_map = {}
        while iLoop < pwd_count:
            is_present, index = kmpAlgo(loginAttempt[previous_index: login_attempt_len], pwd_list[iLoop], suffixPrefixArrayList[iLoop])
            previous_index += index
            if is_present:
                found_string_map[pwd_list[iLoop]] = True
                current_count += len(pwd_list[iLoop])

#             if index != login_attempt_len:
#                 current_len = login_attempt_len - index;
#             else:
            if previous_index == login_attempt_len:
                previous_index = 0
                index = 0
                current_len = login_attempt_len
                iLoop += 1
        
        if current_count >= login_attempt_len:
            print(found_string_map)
        else:
            print("WRONG PASSWORD")
            
                
                
        
    
    
    
    
    
    