'''
Created on May 25, 2017

@author: xdussap
'''
from datetime import datetime

if __name__ == '__main__':
    print(datetime.now());
    for _ in range(1000000000):
        for _ in range(150):
            for _ in range(300):
                pass
    print(datetime.now()); 