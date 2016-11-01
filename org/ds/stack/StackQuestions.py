'''
Created on Oct 3, 2016

@author: Dushyant Sapra
'''
from org.ds.stack.Stack import StackUsingLinkedList


class StackQuestions:
    @staticmethod
    def reverseStringUsingStack(tempString):
        tempStack = StackUsingLinkedList();
        tempList = [];
        for c in tempString:
            tempStack.push(c);

        tempStack.displayIterative();

        while tempStack.top:
            tempList.append(tempStack.pop());
        reversedString = ''.join(tempList);

        print(reversedString);

    def sortStackHelper(self, stack, value, isIncreasing):
        if stack.top is None or (isIncreasing and value < stack.top.data) or (not isIncreasing and value > stack.top.data):
            stack.push(value);
        else:
            tempValue = stack.pop();
            self.sortStackHelper(stack, value, isIncreasing);
            stack.push(tempValue);

    def sortStack(self, stack, isIncreasing=True):
        if stack.top:
            tempValue = stack.pop();
            self.sortStack(stack, isIncreasing);
            self.sortStackHelper(stack, tempValue, isIncreasing);

    def reverseStackHelper(self, stack, value):
        if stack.top is None:
            stack.push(value);
        else:
            tempValue = stack.pop();
            self.reverseStackHelper(stack, value);
            stack.push(tempValue);

    def reverseStack(self, stack):
        if stack.top:
            tempValue = stack.pop();
            self.reverseStack(stack);
            self.reverseStackHelper(stack, tempValue);

    def stockSpanProblem(self, stack):
        print()

if __name__ == '__main__':
    obj = StackQuestions();

    stack = StackUsingLinkedList();
    stack.push("1");
    stack.push("2");
    stack.push("3");
    stack.push("4");

#     obj.reverseStack(stack, "NODE");
#     stack.displayRecursive();
    
    stack = StackUsingLinkedList();
    stack.push(30);
    stack.push(-5);
    stack.push(18);
    stack.push(14);
    stack.push(-3);

    obj.sortStack(stack);
    stack.displayIterative();
    
    obj.reverseStack(stack);
    print("\n")
    stack.displayIterative();