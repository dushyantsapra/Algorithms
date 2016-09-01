'''
Created on Jul 9, 2016

@author: sapra
'''

class Temp:
    def temp(self):
        return 2;

temp = Temp();

if temp.temp() == 1:
    print("1");
else:
    print("0");
    
print(float("inf"))

n = float("inf");

if float("inf") > 0:
    print("A")
    n = 1;
    print(n);
else:
    print("B");