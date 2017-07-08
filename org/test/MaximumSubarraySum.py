'''
Created on Jun 3, 2017

@author: sapra
'''

if __name__ == '__main__':
    inputfile = open("/home/sapra/input.txt")
    test_count = int(inputfile.readline().strip())

    for _ in range(test_count):
        n, k = list(map(int, inputfile.readline().strip().split(" ")))
        num_list = [int(int(num) % k) for num in inputfile.readline().strip().split(' ')]
        
#         print(num_list)
        
        o_sum1 = num_list[0]
        o_sum2 = num_list[n - 1]
        is_first = True
        current_max = 0
        for window_size in range(1, n + 1):
            sum1 = 0
            sum2 = 0
            if not is_first:
                o_sum1 += num_list[window_size - 1]
                o_sum2 += num_list[n - window_size]
            
            is_first = False
            
            sum1 = o_sum1
            sum2 = o_sum2
            
            current_max = max(current_max, int(sum1 % k), int(sum2 % k))
#             print(current_max)
            
            iLoop_s = 0
            iLoop_e = window_size
            
            jLoop_s = n - window_size - 1
            jLoop_e = n - 1;
            while iLoop_s <= jLoop_s:
                sum1 += num_list[iLoop_e] - num_list[iLoop_s]
                sum2 += num_list[jLoop_s] - num_list[jLoop_e]
                current_max = max(current_max, int(sum1 % k), int(sum2 % k))
                
                iLoop_s += 1
                iLoop_e += 1
                
                jLoop_s -= 1
                jLoop_e -= 1
#             print(current_max)
        
#         print()
        print(current_max)
        
        
