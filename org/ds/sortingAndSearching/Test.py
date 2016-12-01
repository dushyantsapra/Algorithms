'''
Created on 31-May-2016

@author: Dushyant
'''
from __builtin__ import str

iValue = 10;
fValue = float(10.00);
sValue = "Dushyant Sapra";
a, b = 3, 5;
print ("Hello");

print("Variables Example");
print("Value of A is %d, Value of B is %d" % (a, b));
print ("Integer Value is %d, Float Value is %f, String Value is %s \n" % (iValue, fValue, sValue));

# tempList = [10, 20, 30];
# tempList.append(1);
# tempList.append(float(10));
# tempList.append("Dushyant Sapra");

tempList = [10];
tempList[0] = 60;

print("List Example");
print(tempList);

print("\nFor Loop Example")
for value in tempList:
    print(value);
    
print("\nWhile Loop Example")
iCount = 1;
while iCount < 2:
    print(iCount);
    iCount += 1;

def myFunction(name="Dushyant", salary=10.00):
    print("Name is %s, Salary is %f" % (name, salary));


myFunction();

for value in range(2):
    print(value);
    
l = ["Hi", "Hello", "Bye"];
print(l)

for s in l[:]:
    if s is "Hello":
        l.remove(s);
print(l)

m = {};
m["V0"] = 0;
m["V1"] = 1;
m["V2"] = 2;

for key in m.iterkeys():
    print(key);

print("\nadasd");

print(m.keys()[0]);

if __name__ == '__main__':
    ll = [];
    iValue = 1;
    for iLoop in range(5):
        if iValue == 1:
            ll.append(list([iLoop]));
            iValue += 1;
        elif iValue == 2:
            ll[len(ll) - 1] = ll[len(ll) - 1].append(iLoop);
            iLoop = 1;
        print(ll); 
    print("Bazingaaaaa");
    print(ll); 

print("\n");
str = "Hello"
print(str[0] + " " + str[len(str) - 1]);