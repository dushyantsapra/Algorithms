'''
Created on 15-Jun-2016

@author: Dushyant
'''
from org.ds.common.SingleLinkedNode import SingleLinkedNode

class Queue:
    def __init__(self):
        self.front = None;
        self.rear = None;
        self.size = 0;

    def enQueue(self, data):
        node = SingleLinkedNode(data);

        if self.rear is None:
            self.front = self.rear = node;
        else:
            self.rear.next = node;
            self.rear = node;
        
        self.size += 1;

    def deQueue(self):
        if self.front is None:
            return None;
        elif self.front is self.rear:
            node = self.front;
            data = node.data;
            self.releaseNodeMemory(node);
            self.front = self.rear = None;
        else:
            node = self.front;
            data = node.data;
            self.front = node.next;
            self.releaseNodeMemory(node);
        
        self.size -= 1;
        return data;

    def queueTraversal(self):
        front = self.front;
        while front is not None:
            print(front.data);
            front = front.next;

    def releaseNodeMemory(self, node):
        node.next = None;
        del node;
    
    def getSize(self):
        return self.size;
    
"""queue = Queue();
queue.enQueue(1);
queue.enQueue(2);
queue.enQueue(3);
queue.enQueue(4);
queue.enQueue(5);
queue.enQueue(6);
queue.queueTraversal();

print("");
queue.deQueue();
queue.deQueue();
queue.deQueue();
queue.queueTraversal();"""