'''
Created on Oct 12, 2016

@author: Dushyant Sapra
'''
class DoublyLinkedNode:
    def __init__(self, data):
        self.previous = None;
        self.next = None;
        self.data = data;

    def __str__(self):
        return "DoublyLinkedNode is " + str(self.data);

    def __eq__(self, other):
        return self.data == other.data;
    
    def __hash__(self):
        return hash(self.data);