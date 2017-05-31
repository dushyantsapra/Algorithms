'''
Created on May 29, 2017

@author: sapra
'''

# 5
# 20 7 8 2 5

if __name__ == '__main__':
    inputfile = open("/home/sapra/input.txt");
    prices = int(inputfile.readline().strip())
    priceList = list(map(int, inputfile.readline().strip().split(" ")))
    
    priceMap = {};
    
    for iLoop in range(prices):
        priceMap[priceList[iLoop]] = iLoop
    
    priceList.sort(reverse=True)
    
    min_loss = float("inf")
    iLoop = 0
    jLoop = 1
    while iLoop < prices - 1:
        if priceMap[priceList[iLoop]] < priceMap[priceList[jLoop]]:
            diff = priceList[iLoop] - priceList[jLoop]
            if min_loss > diff:
                min_loss = diff
            iLoop += 1
            jLoop = iLoop + 1
        elif jLoop < prices - 1:
            jLoop += 1;
        else:
            jLoop = iLoop + 2;
            iLoop += 1;
    
    print(min_loss)
            
            
            
               
