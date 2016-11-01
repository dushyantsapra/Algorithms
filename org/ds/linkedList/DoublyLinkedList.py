'''
Created on Oct 12, 2016

@author: Dushyant Sapra
'''

from org.ds.linkedList.DoublyLinkedNode import DoublyLinkedNode


class DoublyLinkedList:
    def __init__(self):
        self.head = None;
        self.tail = None;
        self.length = 0;
    
    def size(self):
        return self.length;

    def add(self, data):
        node = DoublyLinkedNode(data);
        if self.head is None:
            self.head = self.tail = node;
        else:
            node.previous = self.tail;
            self.tail.next = node;
            self.tail = node;
        self.length += 1;
    
    def displayIterative(self):
        if self.head:
            tempNode = self.head;

            while tempNode is not None:
                print(tempNode.data);
                tempNode = tempNode.next;
        else:
            print("Doubly Linked List is Empty");

if __name__ == '__main__':
    dll = DoublyLinkedList();
    dll.add(1);
    dll.add(2);
    dll.add(3);
    dll.add(4);
    dll.add(5);
    
    dll.displayIterative();