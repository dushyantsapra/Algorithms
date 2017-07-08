'''
Created on Jun 9, 2017

@author: sapra
'''

if __name__ == "__main__":
    inputfile = open("/home/sapra/input.txt")
    test_count = int(inputfile.readline().strip())
    
    for _ in range(test_count):
        a, b, n = list(map(int, inputfile.readline().strip().split(" ")))
        
        cal_arr = list(map(int, inputfile.readline().strip().split(" ")))
        
        x = 0
        y = 0
        
        for cal in cal_arr:
            a_list = []
            if int(a % cal) == 0:
                x = max(x, a // cal)
                a_list.append(int(a % cal))
            
            b_list = []
            if int(b % cal) == 0:
                y = max(y, b // cal)
                b_list.append(int(b % cal))

            curr_sum = 0
            i = 1
            start = 0
            for i in range(1, n):
                while curr_sum > a and start < i - 1:
                    curr_sum = curr_sum - cal_arr[start];
                    start += 1;
             
                if (curr_sum == a): 
                    x = max(x, i - start)
                    
            curr_sum = 0
            i = 1
            start = 0
            for i in range(1, n):
                while curr_sum > b and start < i - 1:
                    curr_sum = curr_sum - cal_arr[start];
                    start += 1;
             
                if (curr_sum == b): 
                    y = max(y, i - start)
        print("{} {}".format(x, y))
