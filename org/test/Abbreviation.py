'''
Created on Jun 4, 2017

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

def kmpAlgo(mainString, subString):
    suffixPrefixArray = computeSuffixWhichIsPrefixOfGivenString(subString);

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
    inputfile = open("/home/sapra/input.txt")
    n = int(inputfile.readline().strip())

    for _ in range(n):
        main_string = inputfile.readline().strip()
        sub_string = inputfile.readline().strip()
        
        main_string_char_list = list(main_string)
        print(main_string_char_list)
        
        main_string_lower = main_string
        main_string_lower = main_string_lower.lower()
        
        sub_string_lower = sub_string
        sub_string_lower = sub_string_lower.lower()
        
        main_string_char_map = {}
        index = 0
        for c in main_string_lower:
            if c not in main_string_char_map:
                main_string_char_map[c] = [index]
            else:
                main_string_char_map[c].append(index)
            index += 1
        
        for key in main_string_char_map.keys():
            main_string_char_map[key].sort()
        
        is_present = True
        index_to_del = []
        for c in sub_string_lower:
            if c not in main_string_char_map:
                is_present = False
                break
            else:
                index_to_del.append(main_string_char_map[c].pop(0))
                if len(main_string_char_map[c]) == 0:
                    del main_string_char_map[c]
        
        index_to_del.sort(key=None, reverse=True)
        print(index_to_del)
        
        for i in index_to_del:
            del main_string_char_list[i]
        
        print(main_string_char_list)
        
        for c in main_string_char_list:
            if ord(c) >= 65 and ord(c) <= 90:
                is_present = False
         
        if is_present:
            print("YES")
        else:
            print("NO")
        
        
        a = []
#         a.insert(index, object)(value, )
            
            






