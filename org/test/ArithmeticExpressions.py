'''
Created on May 31, 2017

@author: xdussap
'''
from os.path import os
import sys


def find_arithmetic_expression(arr, index, current_result, expression):
    operator_list = ["*", "+", "-"]
    current_result = int(current_result % 101)
    if index >= len(arr):
        if current_result == 0:
            return True;
        else:
            return False

    for operator in operator_list:
        if operator == "*":
            expression.append("*")
            current_result = int(current_result * int(arr[index]))
            expression.append(arr[index])
            if find_arithmetic_expression(arr, index + 1, current_result, expression):
                return True;
            else:
                expression.pop()
                expression.pop()
                current_result = int(current_result / int(arr[index]))
        elif operator == "+":
            expression.append("+")
            current_result = int(current_result + int(arr[index]))
            expression.append(arr[index])
            if find_arithmetic_expression(arr, index + 1, current_result, expression):
                return True;
            else:
                expression.pop()
                expression.pop()
                current_result = int(current_result - int(arr[index]))
        elif operator == "-":
            expression.append("-")
            current_result = int(current_result - int(arr[index]))
            expression.append(arr[index])
            if find_arithmetic_expression(arr, index + 1, current_result, expression):
                return True;
            else:
                expression.pop()
                expression.pop()
                current_result = int(current_result + int(arr[index]))

if __name__ == '__main__':
    sys.setrecursionlimit(100000)
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);
    arrLen = int(inputfile.readline().strip())

    arr = list(map(int, inputfile.readline().strip().split(" ")));

    expression = [arr[0]]
    if find_arithmetic_expression(arr, 1, int(arr[0]), expression):
        print(*expression, sep = "")