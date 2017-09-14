'''
Created on Aug 14, 2017

@author: xdussap
'''

def printSubArrayWithGivenSum(inp_arr, given_sum):
    s_index = 0
    e_index = -1
    
    arr_size = len(inp_arr)
    
    curr_sum = 0
    is_present = False
    for value in inp_arr:
        while (curr_sum > given_sum and s_index < arr_size):
            curr_sum -= inp_arr[s_index]
            s_index += 1
        
        if curr_sum == given_sum:
            is_present = True
            break
        
        curr_sum += value
        e_index += 1

    if not is_present:
        print("No Sub Array Present")
    else:
        print("Given Sum Found b/w : {} - {}".format(s_index, e_index))

if __name__ == '__main__':
#     printSubArrayWithGivenSum([6, 5, 3, 1, 8, 7, 2, 4], 10)
    printSubArrayWithGivenSum([15, 2, 4, 8, 9, 5, 10, 23], 23)