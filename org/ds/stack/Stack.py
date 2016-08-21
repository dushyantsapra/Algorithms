'''
Created on Jun 29, 2016

@author: Dushyant Sapra
'''

from org.ds.common.SingleLinkedNode import SingleLinkedNode

class StackUsingLinkedList:
    def __init__(self):
        self.top = None;
        self.size = 0;

    def push(self, data):
        node = SingleLinkedNode(data);
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

    def reverseStackByData(self, head=None):
        if head:
            if head.next:
                self.reverseStackByData(head.next);
                while head.next is not None:
                    head.data = head.next.data + head.data;
                    head.next.data = head.data - head.next.data;
                    head.data = head.data - head.next.data;
                    head = head.next;
            else:
                return;
        else:
            if self.top:
                if self.top.next:
                    self.reverseStackByData(self.top.next);
                    headNode = self.top;
                    while headNode.next is not None:
                        headNode.data = headNode.next.data + headNode.data;
                        headNode.next.data = headNode.data - headNode.next.data;
                        headNode.data = headNode.data - headNode.next.data;
                        headNode = headNode.next;
            else:
                print("Stack is Empty");

    def reverseStackByNode(self, parent=None, head=None):
        if head:
            if head.next:
                self.reverseStackByNode(head, head.next);
                parent.next = head.next;
                tempParent = parent;
                
                while parent.next:
                    parent = parent.next;
                head.next = None;
                parent.next = head;

                parent = tempParent;
            else:
                return;
        else:
            if self.top:
                if self.top.next:
                    self.reverseStackByNode(self.top, self.top.next);

                    tailNode = self.top;
                    self.top = self.top.next;
                    tailNode.next = None;

                    tempHead = self.top;

                    while self.top.next:
                        self.top = self.top.next;

                    self.top.next = tailNode;

                    self.top = tempHead;

            else:
                print("Stack is Empty");

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

# *********************StackUsingLinkedList****************************
"""stack = StackUsingLinkedList();
stack.push(1);
stack.push(2);
stack.push(3);

stack.displayIterative();
print();
stack.displayRecursive();

stack.reverseStackByNode();
print();
stack.displayIterative();"""

# StackUsingLinkedList.reverseStringUsingStack("Hello");
# *********************StackUsingLinkedList****************************
