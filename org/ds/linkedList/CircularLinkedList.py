'''
Created on Jun 29, 2016

@author: Dushyant Sapra
'''
from org.ds.linkedList.SinglyLinkedNode import SinglyLinkedNode


class CircularLinkedList:
    def __init__(self):
        self.head = None;
        self.tail = None;
        self.length = 0;
    
    def add(self, data):
        node = SinglyLinkedNode(data);
        if self.head is None:
            self.head = self.tail = node;
            node.next = self.head;
        else:
            self.tail.next = node;
            self.tail = node;
            self.tail.next = self.head;
        self.length += 1;
        
    def displayIterative(self):
        if self.head:
            tempNode = self.head;
            
            while tempNode is not None:
                print(tempNode.data);
                if tempNode.next is not self.head:
                    tempNode = tempNode.next;
                else:
                    break;
        else:
            print("Linked List is Empty");
    
    def displayRecursive(self, head=None):
        if head:
            print(head.data);
            if head.next is not self.head:
                return self.displayRecursive(head.next);
            else:
                return;
        else:
            if self.head:
                print(self.head.data);
                if self.head.next is not self.head:
                    return self.displayRecursive(self.head.next);
                else:
                    return;
            else:
                print("Linked List is Empty");

    def sortedAdd(self, data):
        node = SinglyLinkedNode(data);
        if self.head is None:
            self.head = self.tail = node;
            node.next = self.head;
        elif self.head.data > data:
            node.next = self.head;
            self.tail.next = node;
            self.head = node;
        elif self.tail.data < data:
            self.tail.next = node;
            self.tail = node;
            self.tail.next = self.head;
        else:
            tempNode = self.head;
            while tempNode:
                if tempNode.next.data > data:
                    node.next = tempNode.next;
                    tempNode.next = node;
                    break;
                else:
                    tempNode = tempNode.next;
        self.length += 1;

circularLL = CircularLinkedList();
circularLL.sortedAdd(10);
circularLL.sortedAdd(30);
circularLL.sortedAdd(50);
circularLL.sortedAdd(70);
circularLL.sortedAdd(90);

# circularLL.displayIterative();

circularLL.sortedAdd(80);
circularLL.displayIterative();
