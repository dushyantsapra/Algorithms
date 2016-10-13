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

print("\n");
for iLoop in range(1, 5):
    print(iLoop);
    
g = [[0 for y in range(2)] for x in range(2)];

print("\n");
for iValue in range(0, len(g)):
    for jValue in range(0, len(g[iValue])):
        print(g[iValue][jValue]);
        
m = {};
str = "Hello";
str1 = "Bye";

m[str] = 1;
m[str1] = 2;

print("\n\n");
print(m.keys()[1])