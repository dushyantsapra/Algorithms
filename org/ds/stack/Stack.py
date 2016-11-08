'''
Created on Jun 29, 2016

@author: Dushyant Sapra
'''

from org.ds.linkedList.SinglyLinkedNode import SinglyLinkedNode


class StackUsingLinkedList:
    def __init__(self):
        self.top = None;
        self.size = 0;

    def getTop(self):
        if self.top:
            return self.top.data;
        else:
            return None;

    def push(self, data):
        node = SinglyLinkedNode(data);
        if self.top is None:
            self.top = node;
        else:
            node.next = self.top;
            self.top = node;
        self.size += 1;

    def pop(self):
        if self.top:
            data = self.top.data;
            self.top = self.top.next;
            self.size -= 1;
            return data;
        else:
            print("Stack is Empty");

    def getSize(self):
        return self.size;

#     Display data in Order of Removal
    def displayIterative(self):
        if self.top:
            tempNode = self.top;

            while tempNode is not None:
                print(tempNode.data);
                tempNode = tempNode.next;
        else:
            print("Stack is Empty");

#     Display data in Order of Insertion
    def displayRecursive(self, top=None):
        if top:
            if top.next:
                self.displayRecursive(top.next);
            print(top.data);
        else:
            if self.top:
                if self.top.next:
                    self.displayRecursive(self.top.next);
                print(self.top.data);
            else:
                print("Stack is Empty");

    def contains(self, data):
        if self.top:
            tempNode = self.top;

            while tempNode is not None:
                if tempNode.data == data:
                    return True;
                tempNode = tempNode.next;
        else:
            return False;

class StackUsingArray:
    def __init__(self, maxSize):
        self.stack = [];
        self.maxSize = maxSize;
        self.currentSize = 0;
        
    def push(self, data):
        if self.currentSize == self.maxSize:
            print("Stack OverFlow");
            return;
        else:
            self.stack.append(data);
            self.currentSize += 1;
            
    def pop(self):
        if self.currentSize == 0:
            print("Stack is Empty");
            return;
        else:
            self.currentSize -= 1;
            return self.pop(0);

    def display(self):
        if self.currentSize == 0:
            print("Stack is Empty");
            return;
        else:
            for data in self.stack:
                print(data);

if __name__ == '__main__':

    stack = StackUsingLinkedList();
    stack.push(1);
    stack.push(2);
    stack.push(3);
    
    stack.displayIterative();
    print();
    stack.displayRecursive();