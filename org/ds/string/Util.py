'''
Created on Mar 22, 2017

@author: xdussap
'''
from _collections import OrderedDict
from copy import deepcopy


class Util:
    @staticmethod
    def string_permutation_helper(str_size, char_count_map, temp_arr, string_permutaion_list):
        for key, value in char_count_map.items():
            if value > 0:
                temp_arr.append(key);
                char_count_map[key] -= 1;
                Util.string_permutation_helper(str_size, char_count_map, temp_arr, string_permutaion_list);
                char_count_map[key] += 1;
                temp_arr.pop();
        if len(temp_arr) == str_size:
            string_permutaion_list.append(''.join(deepcopy(temp_arr)));
        return;

    """
        Formula
        n = lenght of String.
        Say String contains m char(say x is repeated 2 times, y is repeated 3 times, z is repeated 2 times) with repetition
        permutations = n!/(2! * 3! * 2!)
    """
    @staticmethod
    def stringPermutation(orgString):
        char_count_map = {};
        for temp_char in orgString:
            if temp_char not in char_count_map:
                char_count_map[temp_char] = 1;
                continue;
            char_count_map[temp_char] += 1;

        char_count_map = OrderedDict(sorted(char_count_map.items(), key=lambda t: t[0]));

        temp_arr = [];
        string_permutaion_list = [];
        Util.string_permutation_helper(len(orgString), char_count_map, temp_arr, string_permutaion_list)
#         print(len(string_permutaion_list))
        print(string_permutaion_list)

#         print(char_count_map);

if __name__ == '__main__':
    orgString = "AABEEF";
#     print(orgString);

    Util.stringPermutation(orgString);
