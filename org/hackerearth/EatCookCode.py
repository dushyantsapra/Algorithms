'''
Created on Jun 9, 2017

@author: sapra
'''

if __name__ == "__main__":
    inputfile = open("/home/sapra/input.txt")
    test_count = int(inputfile.readline().strip())
    
    x = 0
    y = 0
    flag = False
    is_first = True
    previous_count = 0
    for _ in range(test_count):
        inputstring = inputfile.readline().strip()
        
        c = inputstring[0]
        curr_x = 0
        max_x = 0
        for e in inputstring:
            if e == 'C':
                curr_x += 1
            else:
                max_x = max(max_x, curr_x)
                curr_x = 0
        max_x = max(max_x, curr_x)
        x = max(max_x, x)
        
        max_y = 0;
        if previous_count > 0:
            max_y = previous_count
            for e in inputstring:
                if e == 'C':
                    previous_count += 1
                else:
                    break
             
            if previous_count > max_y:
                y = max(y, previous_count)
 
        previous_count = 0
        if inputstring[len(inputstring) - 1] == 'C':
            iLoop = len(inputstring) - 1
            while iLoop > 0:
                if inputstring[iLoop] == 'C':
                    previous_count +=1
                else:
                    break
                iLoop -= 1
                
        
    print("{} {}".format(x, y))
        
