'''
Created on Aug 14, 2017

@author: xdussap
'''

def sub_array_with_max_sum(inp_arr):
    max_i = 0
    max_j = 0
    curr_i = 0
    curr_j = 0
    
    max_so_far = inp_arr[0]
    curr_max = inp_arr[0]
    
    arr_size = len(inp_arr)
    
    for index in range(1, arr_size):
        if inp_arr[index] > max_so_far + inp_arr[index]:
            max_so_far = inp_arr[index]
            curr_i = index
            curr_j = index
        else:
            max_so_far += inp_arr[index]
            curr_j = index

        if curr_max < max_so_far:
            curr_max = max_so_far
            max_i = curr_i
            max_j = curr_j 
#             sub_array_e_index = index
    
    print("Max Sum is : {}, sIndex : {}, eIndex : {}".format(curr_max, max_i, max_j))

if __name__ == '__main__':
    sub_array_with_max_sum([-2, -3, 4, -1, -2, 1, 5, -3])
    sub_array_with_max_sum([-10, -2, -3, -4, -1, -2, -13, -5, -3])
    sub_array_with_max_sum([-6, -5, -3, 1, -8, -7, -2, -4])
    
    
    
    