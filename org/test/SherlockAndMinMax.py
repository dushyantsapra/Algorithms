'''
Created on May 17, 2017

@author: sapra
'''

if __name__ == '__main__':
    inputfile = open("/home/sapra/input.txt");
    arrLen = int(inputfile.readline().strip());

    originlArr = list(map(int, inputfile.readline().strip().split(" ")));
    originlArr = sorted(originlArr)

    print(originlArr)

    startrange, endrange = list(map(int, inputfile.readline().strip().split(" ")));

    maxOfMin = (float("-inf"), -1);
#     Completely Covering
    if originlArr[0] > startrange and originlArr[arrLen - 1] < endrange:
        maxOfMin = ((originlArr[0] - startrange), startrange)
        index = 1;
        while index < arrLen - 1:
            currdiff = int((originlArr[index] - originlArr[index - 1]) / 2)
            if currdiff > maxOfMin[0]:
                maxOfMin = (currdiff, (originlArr[index] + currdiff));
        currdiff = int(endrange - originlArr[index])
        if currdiff > maxOfMin[0]:
            maxOfMin = (currdiff, (originlArr[index] + currdiff));
#     Completely Covered
    elif originlArr[0] < startrange and originlArr[arrLen - 1] > endrange:
        index = 0;
        startIndex = 0;
        endIndex = 0;
        while index < arrLen:
            if originlArr[index] < startrange:
                startIndex = index;
            elif originlArr[index] > endrange:
                endIndex = index;
                break;
        
        diff1 = startrange - originlArr[startIndex];
        diff2 = originlArr[startIndex + 1] - startrange
        maxOfMin = (diff1, startrange) if diff1 < diff2 else (diff2, startrange)
        
        index = startIndex + 1
        
                
#     start out, end in
    elif originlArr[0] > startrange and originlArr[arrLen - 1] > endrange:
        pass
#     start in, end out
    elif originlArr[0] < startrange and originlArr[arrLen - 1] < endrange:
        pass

    print(maxOfMin[1])
