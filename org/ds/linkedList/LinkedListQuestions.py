'''
Created on Oct 5, 2016

@author: Dushyant Sapra
'''

from org.ds.linkedList.SinglyLinkedList import SinglyLinkedList
from org.ds.stack.Stack import StackUsingLinkedList


class LinkedListQuestions:
    @staticmethod
    def reverseSingleLinkedListByReference(ll):
        if ll.head:
            tempNode = ll.head;

            ll.head = ll.head.next;
            tempNode.next = None;

            LinkedListQuestions.reverseSingleLinkedListByReference(ll);

            if ll.head == None:
                ll.head = tempNode;
                ll.tail = tempNode;
            else:
                ll.tail.next = tempNode;
                ll.tail = tempNode;

    @staticmethod
    def reverseSingleLinkedList(ll):
        LinkedListQuestions.reverseSingleLinkedListByReference(ll);
        
    @staticmethod
    def reverseFirstKElementOfSingleLinkedListHelper(ll, size, loopCount=0, lastNode=None):
        if ll.head:
            tempNode = ll.head;

            ll.head = ll.head.next;
            tempNode.next = None;

            loopCount += 1;
            if loopCount < size:
                LinkedListQuestions.reverseFirstKElementOfSingleLinkedListHelper(ll, size, loopCount, lastNode);

            if loopCount == size:
                ll.head = tempNode;
                lastNode = ll.head;
            else:
                tempNode.next = lastNode.next;
                lastNode.next = tempNode;
            loopCount -= 1;

    @staticmethod
    def reverseFirstKElementOfSingleLinkedList(ll, size):
        if size == 1:
            return;

        if size == ll.size():
            LinkedListQuestions.reverseSingleLinkedListByReference(ll);

        LinkedListQuestions.reverseFirstKElementOfSingleLinkedListHelper(ll, size);

    @staticmethod
    def detectLoopInLinkedList(ll):
        intersectionNode = None;
        singleJumper = ll.head;
        doubleJumper = ll.head;

        while (singleJumper != None and doubleJumper != None):
            singleJumper = singleJumper.next;
            if doubleJumper.next and doubleJumper.next.next:
                doubleJumper = doubleJumper.next.next;
            else:
                break;

            if singleJumper == doubleJumper:
                intersectionNode = singleJumper;
                break;
        return intersectionNode;

    @staticmethod
    def removeLoopInLinkedList(ll, node):
        node1 = ll.head;
        node2 = node;

#         Finding Start of the Loop
        while (node1 is not node2):
            node1 = node1.next;
            node2 = node2.next;

        print("Loop Found at " + str(node1.data));

#         Get to the last Node of the linkedList
        while node2.next != node1:
            node2 = node2.next;

#         Remove the Loop
        node2.next = None;

#     Find If Loop Exists, If Exists then the 'intersectionNode' would always be b/w the start of Loop and 
#     end of LinkedList.
#     For Example for List 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#     If loop is at 4 then intersection would be 8
#     If loop is at 7 then intersection would be 7
    @staticmethod
    def detectAndRemoveLoopInLinkedList(ll):
        intersectionNode = LinkedListQuestions.detectLoopInLinkedList(ll);
        if intersectionNode:
            LinkedListQuestions.removeLoopInLinkedList(ll, intersectionNode);
        else:
            print("No Loop Found");

    @staticmethod
    def mergeTwoSortedListIteratively(list1, list2, ll):
        tempList1 = list1.head;
        tempList2 = list2.head;

        while tempList1 and tempList2:
            if tempList1.data <= tempList2.data:
                ll.add(tempList1.data);
                tempList1 = tempList1.next;
            else:
                ll.add(tempList2.data);
                tempList2 = tempList2.next;

        while tempList1:
            ll.add(tempList1.data);
            tempList1 = tempList1.next;

        while tempList2:
            ll.add(tempList2.data);
            tempList2 = tempList2.next;

    @staticmethod
    def mergeTwoSortedListrecursivelyHelper(list1, list2, ll):
        if list1 is None:
            while list2:
                ll.add(list2.data);
                list2 = list2.next;
            return;

        if list2 is None:
            while list2:
                ll.add(list2.data);
                list1 = list1.next;
            return;

        if list1.data <= list2.data:
            ll.add(list1.data);
            LinkedListQuestions.mergeTwoSortedListrecursivelyHelper(list1.next, list2, ll);
        else:
            ll.add(list2.data);
            LinkedListQuestions.mergeTwoSortedListrecursivelyHelper(list1, list2.next, ll);

    @staticmethod
    def mergeTwoSortedListrecursively(list1, list2, ll):
        LinkedListQuestions.mergeTwoSortedListrecursivelyHelper(list1.head, list2.head, ll);

    @staticmethod
    def checkIfLinkedListIsPalindrome(ll):
        stack = StackUsingLinkedList();

        tempNode = ll.head;

        while tempNode is not None:
            stack.push(tempNode.data);
            tempNode = tempNode.next;

        tempNode = ll.head;

        isPalindrome = True;
        while tempNode is not None:
            if tempNode.data == stack.pop():
                tempNode = tempNode.next;
                continue;
            else:
                isPalindrome = False;
                break;

        if isPalindrome:
            print("LL is Palindrome");
        else:
            print("LL is not Palindrome");
        return isPalindrome;

    @staticmethod
    def deleteAltNodes(ll):
        nodeToDelete = None;

        sNode = ll.head;

        while sNode is not None and sNode.next is not None:
            nodeToDelete = sNode.next;
            sNode.next = sNode.next.next;
            sNode = sNode.next;

            del nodeToDelete;

        print("\nLinkedList After Deleting Alternative Nodes");
        ll.displayIterative();

    @staticmethod    
    def createLLFromIntersectionOfTwoSortedList(ll1, ll2):
        ll = SinglyLinkedList();
        ll1Node = ll1.head;
        ll2Node = ll2.head;
        while ll1Node is not None and ll2Node is not None:
            if ll1Node.data == ll2Node.data:
                ll.add(ll1Node.data);
                ll1Node = ll1Node.next;
                ll2Node = ll2Node.next;
            elif ll1Node.data < ll2Node.data:
                ll1Node = ll1Node.next;
            else:
                ll2Node = ll2Node.next;

        print("\nNew Linked List Created Using Intersection Of Two Sorted List");
        ll.displayIterative();

    @staticmethod
    def pairwiseSwapElements(ll):
        sNode = ll.head;
        
        while sNode is not None and sNode.next is not None:
            sNode.data = sNode.data + sNode.next.data;
            sNode.next.data = sNode.data - sNode.next.data;
            sNode.data = sNode.data - sNode.next.data;

            sNode = sNode.next.next;

        print("\nLL after Pairwise Swaped Elements");
        ll.displayIterative();

    @staticmethod
    def removeDuplicatesInSortedListHelper(ll, sNode):
        nodeToDelete = None;
        if sNode is not None and sNode.next is not None:
            if sNode.data == sNode.next.data:
                nodeToDelete = sNode.next;
                sNode.next = sNode.next.next;
                del nodeToDelete;
            else:
                sNode = sNode.next;
            LinkedListQuestions.removeDuplicatesInSortedListHelper(ll, sNode);

    @staticmethod
    def removeDuplicatesInSortedList(ll):
        sNode = ll.head;
        LinkedListQuestions.removeDuplicatesInSortedListHelper(ll, sNode);

        print("\nLL After Deleting Duplicate Elements");
        ll.displayIterative();

    @staticmethod
    def findMiddleOfLL(ll):
        singleJumper = ll.head;
        doubleJumper = ll.head;

        while singleJumper is not None and doubleJumper is not None:
            singleJumper = singleJumper.next;
            doubleJumper = doubleJumper.next.next;

        print("\nMiddle Node is " + str(singleJumper.data));

    @staticmethod
    def alternatingSplit(ll):
        sNode = ll.head;
        newll = SinglyLinkedList();

        while sNode is not None and sNode.next is not None:
            newll.add(sNode.next.data);
            sNode.next = sNode.next.next;
            sNode = sNode.next;
        
        print("\nAlternatingSplit");
        print("Original List");
        ll.displayIterative();
        print("Alternative Node List");
        newll.displayIterative();

if __name__ == '__main__':
    ll = SinglyLinkedList();
    ll.add("1");
    ll.add("2");
    ll.add("3");

    print("Reversed Linked List")
    LinkedListQuestions.reverseSingleLinkedList(ll);

    print("\n")
    ll.displayIterative();


    ll = SinglyLinkedList();
    ll.add(1);
    ll.add(2);
    ll.add(3);
    ll.add(4);
    node = ll.tail;
    ll.add(5);
    ll.add(6);
    ll.add(7);
    ll.add(8);
    ll.add(9);
    ll.add(10);
    ll.tail.next = node;
    
    LinkedListQuestions.detectAndRemoveLoopInLinkedList(ll);
    ll.displayIterative();
    
    
    list1 = SinglyLinkedList();
    list1.add(1);
    list1.add(3);
    list1.add(5);
    
    list2 = SinglyLinkedList();
    list2.add(2);
    list2.add(4);
    list2.add(6);
    
    finalList = SinglyLinkedList();
    print("\n")
#     LinkedListQuestions.mergeTwoSortedListIteratively(list1, list2, finalList);
    LinkedListQuestions.mergeTwoSortedListrecursively(list1, list2, finalList);
    finalList.displayIterative();
    
    
    ll = SinglyLinkedList();
    ll.add(1);
    ll.add(2);
    ll.add(1);
    LinkedListQuestions.checkIfLinkedListIsPalindrome(ll);
    
    ll = SinglyLinkedList();
    ll.add(1);
    ll.add(2);
    ll.add(3);
#     ll.add(4);
#     ll.add(5);
#     ll.add(6);
#     ll.add(7);
    LinkedListQuestions.deleteAltNodes(ll);

    ll1 = SinglyLinkedList();
    ll2 = SinglyLinkedList();
    ll1.add(1);
    ll1.add(2);
    ll1.add(3);
    ll1.add(4);
    ll1.add(6);

    ll2.add(2);
    ll2.add(4);
    ll2.add(6);
    ll2.add(8);

    LinkedListQuestions.createLLFromIntersectionOfTwoSortedList(ll1, ll2);
    
    
    ll = SinglyLinkedList();
    ll.add(1);
    ll.add(2);
    ll.add(3);
    ll.add(4);
    LinkedListQuestions.pairwiseSwapElements(ll);
    
    ll = SinglyLinkedList();
    ll.add(11);
    ll.add(11);
    ll.add(11);
    ll.add(21);
    ll.add(43);
    ll.add(43);
    ll.add(60);
    LinkedListQuestions.removeDuplicatesInSortedList(ll);
    
    
    ll = SinglyLinkedList();
    ll.add(1);
    ll.add(2);
    ll.add(3);
    ll.add(4);
    ll.add(5);
    ll.add(6);
    ll.add(7);
    LinkedListQuestions.alternatingSplit(ll);
    
    LinkedListQuestions.findMiddleOfLL(ll);
    
    ll = SinglyLinkedList();
    ll.add(1);
    ll.add(2);
    ll.add(3);
    ll.add(4);
    ll.add(5);
    LinkedListQuestions.reverseFirstKElementOfSingleLinkedList(ll, 3);
    print("\nLL After Reversing First " + str(3) + " Nodes");
    ll.displayIterative();
