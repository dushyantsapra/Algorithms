'''
Created on 28-Jun-2016

@author: Dushyant Sapra
'''

from org.competitiveProgramming.Utility import Utility
from org.ds.common.SingleLinkedNode import SingleLinkedNode
from org.ds.stack import Stack
from plainbox.impl.secure.config import IValidator


class SinglyLinkedList:

    def __init__(self):
        self.head = None;
        self.tail = None;
        self.length = 0;

    def add(self, data):
        node = SingleLinkedNode(data);
        if self.head is None:
            self.head = self.tail = node;
        else:
            self.tail.next = node;
            self.tail = node;
        self.length += 1;

    def sortedAdd(self, data):
        node = SingleLinkedNode(data);
        if self.head is None:
            self.head = self.tail = node;
        elif self.head.data > data:
            node.next = self.head;
            self.head = node;
        elif self.tail.data < data:
            self.tail.next = node;
            self.tail = node;
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

    def displayIterative(self):
        if self.head:
            tempNode = self.head;
            
            while tempNode is not None:
                print(tempNode.data);
                tempNode = tempNode.next;
        else:
            print("Linked List is Empty");

    def displayRecursive(self, head=None):
        if head:
            print(head.data);
            if head.next:
                return self.displayRecursive(head.next);
            else:
                return;
        else:
            if self.head:
                print(self.head.data);
                if self.head.next:
                    return self.displayRecursive(self.head.next);
                else:
                    return;
            else:
                print("Linked List is Empty");

    def removeUsingData(self, data):
        currentNode = self.head;
        previousNode = None;

        while currentNode is not None:
            if currentNode.data == data:
                if currentNode is not self.head:
                    previousNode.next = currentNode.next;
                else:
                    self.head = self.head.next;
                break;
            previousNode = currentNode;
            currentNode = currentNode.next;
        self.length -= 1;

    def removeUsingIndex(self, index):
        currentNode = self.head;
        previousNode = self.head;
        tempData = None;
        currentIndex = 0;
        
        if index < self.length:
            while currentNode is not None:
                if currentIndex == index:
                    if currentNode is not self.head:
                        tempData = currentNode.data;
                        previousNode.next = currentNode.next;
                    else:
                        tempData = currentNode.data;
                        self.head = self.head.next;
                    break;
                currentIndex += 1;
                previousNode = currentNode;
                currentNode = currentNode.next;
            self.length -= 1;
        else:
            print("Index out of Bound");
        return tempData;

    def lengthIterative(self):
        length = 0;
        tempNode = self.head;
        while tempNode is not None:
            length += 1;
            tempNode = tempNode.next;
        return length;

    def lengthRecursive(self, head=None):
        if head:
            if head.next:
                return self.lengthRecursive(head.next) + 1;
            else:
                return 1;
        else:
            if self.head:
                if self.head.next:
                    return self.lengthRecursive(self.head.next) + 1;
                else:
                    return 1;
            else:
                print("Linked List is Empty");
                return 0;

    def containsIterative(self, data):
        tempNode = self.head;

        while tempNode is not None:
            if tempNode.data == data:
                return True;
            tempNode = tempNode.next;
        return False;

    def containsRecursive(self, data, head=None):
        if head:
            if head.data == data:
                return True;
            else:
                if head.next:
                    return self.containsRecursive(data, head.next);
                else:
                    return False;
        else:
            if self.head:
                if self.head.data == data:
                    return True;
                else:
                    if self.head.next:
                        return self.containsRecursive(data, self.head.next);
                    else:
                        return False;
            else:
                return False;

#     Swap nodes in a linked list without swapping data
    def swapNodes(self, data1, data2):
        fPrevNode, fNode = None, None;
        lPrevNode, lNode = None, None;

        if data1 == data2:
            return self;

        tempNode = self.head;
        while tempNode is not None:
            if tempNode.data == data1:
                if fNode is not self.head:
                    fNode = tempNode;
                else:
                    fNode = fPrevNode = self.head;
                break;
            fPrevNode = tempNode;
            tempNode = tempNode.next;

        tempNode = self.head;
        while tempNode is not None:
            if tempNode.data == data2:
                if tempNode != self.head:
                    lNode = tempNode;
                else:
                    lNode = lPrevNode = self.head;
                break;
            lPrevNode = tempNode;
            tempNode = tempNode.next;

        if fNode.next is lNode:
            if fNode is self.head:
                self.head = lNode;
                tempNode = fNode.next;
                fNode.next = lNode.next;
                lNode.next = tempNode;
            else:
                print();
        else:
            tempNode = fNode.next;  # 3

            fNode.next = lNode.next;  # 1-2-4
            lNode.next = tempNode; 

            tempNode = fPrevNode.next;
            fPrevNode.next = lNode;
            lPrevNode.next = tempNode;

    def printMiddleNode(self):
        singleJumper = self.head;
        doubleJumber = self.head;

        while doubleJumber.next is not None and doubleJumber.next.next is not None:
            singleJumper = singleJumper.next;
            doubleJumber = doubleJumber.next.next;

        print("Middle Node is %d " % (singleJumper.data));

    def printNthFromLastNode(self, number):
        length = self.length;
        tempNode = self.head;
        jumperNode = self.head;

        iCount = 0;

        if (length - number) == 0:
            print(self.head.data);
            return;
        elif ((length - number) > 0) and number > 0:
            while iCount < number:
                jumperNode = jumperNode.next;
                iCount += 1;

            while jumperNode is not None:
                tempNode = tempNode.next;
                jumperNode = jumperNode.next;
        else:
            print("Selected Number out of Range");
            return;

        print(tempNode.data);
        return;

    def reverseLinkedListByData(self, head=None):
        if head:
            if head.next:
                self.reverseLinkedListByData(head.next);
                while head.next is not None:
                    head.data = head.next.data + head.data;
                    head.next.data = head.data - head.next.data;
                    head.data = head.data - head.next.data;
                    head = head.next;
            else:
                return;
        else:
            if self.head:
                if self.head.next:
                    self.reverseLinkedListByData(self.head.next);
                    headNode = self.head;
                    while headNode.next is not None:
                        headNode.data = headNode.next.data + headNode.data;
                        headNode.next.data = headNode.data - headNode.next.data;
                        headNode.data = headNode.data - headNode.next.data;
                        headNode = headNode.next;
            else:
                print("Linked List is Empty");

    def reverseLinkedListByNode(self, parent=None, head=None):
        if head:
            if head.next:
                self.reverseLinkedListByNode(head, head.next);
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
            if self.head:
                if self.head.next:
                    self.reverseLinkedListByNode(self.head, self.head.next);
                    
                    tailNode = self.head;
                    self.head = self.head.next;
                    tailNode.next = None;
                    
                    tempHead = self.head;
                    
                    while self.head.next:
                        self.head = self.head.next;
                    
                    self.head.next = tailNode;
                    
                    self.head = tempHead;
                    self.tail = tailNode; 
                    
            else:
                print("Linked List is Empty");

    def mergeTwoSortedListIteratively(self, list1, list2):
        tempList1 = list1.head;
        tempList2 = list2.head;

        while tempList1 and tempList2:
            if tempList1.data <= tempList2.data:
                self.add(tempList1.data);
                tempList1 = tempList1.next;
            else:
                self.add(tempList2.data);
                tempList2 = tempList2.next;

        while tempList1:
            self.add(tempList1.data);
            tempList1 = tempList1.next;

        while tempList2:
            self.add(tempList2.data);
            tempList2 = tempList2.next;

    def mergeTwoSortedListrecursivelyHelper(self, list1, list2):
        if list1 is None:
            while list2:
                self.add(list2.data);
                list2 = list2.next;
            return;

        if list2 is None:
            while list2:
                self.add(list2.data);
                list1 = list1.next;
            return;

        if list1.data <= list2.data:
            self.add(list1.data);
            self.mergeTwoSortedListrecursivelyHelper(list1.next, list2);
        else:
            self.add(list2.data);
            self.mergeTwoSortedListrecursivelyHelper(list1, list2.next);

    def mergeTwoSortedListrecursively(self, list1, list2):
        self.mergeTwoSortedListrecursivelyHelper(list1.head, list2.head);

#     Input 1->2->3->4->5->6
#     if k is 4
#     Output Would Be 5->6->1->2->3->4
    def rotateLinkedListCounterClockWiseByKNodes(self, k):
        if k >= self.length:
            print("Number out of range");
            return;

        tempNode = self.head;
        prevNode = None;
        for iLoop in range(k):
            prevNode = tempNode;
            tempNode = tempNode.next;
            iLoop += 1;

        tempHead = self.head;
        self.head = tempNode;
        prevNode.next = None;
        self.tail.next = tempHead;
    
    def reverseLinkedListInGroupsOfGivenSizeByDataHelper(self, k):
        print()

    def reverseLinkedListInGroupsOfGivenSizeByData(self, k):
        if self.head is None:
            return;
        groupList = Utility.fetchGroupofN(len(self.head), k);

    def reverseLinkedListInGroupsOfGivenSizeByNodeHelper(self, k):
        print()

    def reverseLinkedListInGroupsOfGivenSizeByNode(self, k):
        print()

    def removeLoopInLinkedList(self, node):
        node1 = self.head;
        node2 = node;

#         Finding Start of the Loop
        while (node1 is not node2):
            node1 = node1.next;
            node2 = node2.next;

#         Get to the last Node of the linkedList
        while node2.next != node1:
            node2 = node2.next;
        
#         Remove the Loop
        node2.next = None;

    def detectLoopInLinkedList(self):
        singleJumper = self.head;
        doubleJumper = self.head;

        while (singleJumper != None and doubleJumper != None):
            singleJumper = singleJumper.next;
            if doubleJumper.next and doubleJumper.next.next:
                doubleJumper = doubleJumper.next.next;
            else:
                return None;

            if singleJumper == doubleJumper:
                return singleJumper;

#     Find If Loop Exists, If Exists then the 'intersectionNode' would always be b/w the start of Loop and 
#     end of LinkedList.
#     For Example for List 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#     If loop is at 4 then intersection would be 8
#     If loop is at 7 then intersection would be 7
    def detectAndRemoveLoopInLinkedList(self):
        intersectionNode = self.detectLoopInLinkedList();
        if intersectionNode:
            print("Loop Found");
            self.removeLoopInLinkedList(intersectionNode);
        else:
            print("No Loop Found");

    def checkIfLinkedListIsPalindrome(self):
        stack = Stack();

        tempNode = self.head;

        while tempNode is not None:
            stack.push(tempNode.data);
            tempNode = tempNode.next;

        tempNode = self.head;

        isPalindrome = True;
        while tempNode is not None:
            if tempNode.data == stack.pop():
                tempNode = tempNode.next;
                continue;
            else:
                isPalindrome = False;
                break;
        return isPalindrome;

    def fetchNodeAtIndex(self, index):
        tempNode = self.head;
        nodeAtIndex = tempNode;
        iValue = 0;
        while iValue in range((index - 1)):
            nodeAtIndex = tempNode.next;
            iValue += 1;
        return nodeAtIndex;

    def mergeSortHelper(self, sNode, eNode, length):
        if length == 1:
            return sNode;
        elif length == 2:
            if sNode.data > eNode.data:
                sNode.data = sNode.data + eNode.data;
                eNode.data = sNode.data - eNode.data;
                sNode.data = sNode.data - eNode.data;
            return sNode;

        if length / 2 == 0:
            midIndex = int (length / 2) - 1;
        else:
            midIndex = int (length / 2);

        self.mergeSortHelper(sNode, midIndex, length / 2);
        self.mergeSortHelper(midIndex + 1, eNode, tempList);
        self.mergeHelper(startIndex, endIndex, tempList);

        return None;

    def mergeSort(self):
        if self.head:
            self.head = self.mergeSortHelper(self.head, self.tail, self.length);
        else:
            print("Linked List is Empty");
            return;

linkedList = SinglyLinkedList();
linkedList.add(10);
linkedList.add(20);
linkedList.add(30);
linkedList.add(40);
linkedList.add(50);
linkedList.add(60);

################## Sorted Insert Example Start####################
sortedList = SinglyLinkedList();
sortedList.sortedAdd(20);
sortedList.sortedAdd(10);
sortedList.sortedAdd(40);
sortedList.sortedAdd(50);
sortedList.sortedAdd(30);
sortedList.displayIterative();
################## Sorted Insert Example Ends####################

################## Check if LinkedList is Palindrome Start####################
pLL = SinglyLinkedList();
pLL.add(1);
pLL.add(2);
pLL.add(3);
pLL.add(1);
pLL.add(1);

print("isPalindrome %s" % (pLL.checkIfLinkedListIsPalindrome()));
################## Sorted Insert Example Ends####################

################## DetectAndRemoveLoop Start####################
linkedList.head = SingleLinkedNode(10);
headNode = linkedList.head;

node = SingleLinkedNode(20);
headNode.next = node;
headNode.next.next = SingleLinkedNode(30);
headNode.next.next.next = SingleLinkedNode(40);
node1 = SingleLinkedNode(50);
node1.next = node;
headNode.next.next.next.next = node1;

linkedList.detectAndRemoveLoopInLinkedList();
linkedList.displayIterative();
################## DetectAndRemoveLoop Ends####################

# linkedList.reverseLinkedListByData();
# linkedList.reverseLinkedListByNode();
# linkedList.displayIterative();

# linkedList.rotateLinkedListCounterClockWiseByKNodes(6);
# linkedList.displayIterative();

"""list1 = SinglyLinkedList();
list1.add(1);
list1.add(3);
list1.add(5);

list2 = SinglyLinkedList();
list2.add(2);
list2.add(4);
list2.add(6);

finalList = SinglyLinkedList();
finalList.mergeTwoSortedList(list1, list2);
finalList.mergeTwoSortedListrecursively(list1, list2);
finalList.displayIterative();"""
