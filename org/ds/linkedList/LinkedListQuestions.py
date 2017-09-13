'''
Created on Oct 5, 2016

@author: Dushyant Sapra
'''

from org.ds.linkedList.SinglyLinkedList import SinglyLinkedList
from org.ds.linkedList.SinglyLinkedNode import SinglyLinkedNode
from org.ds.stack.Stack import StackUsingLinkedList
from org.ds.linkedList.DoublyLinkedList import DoublyLinkedList


class LinkedListQuestions:
    @staticmethod
#     Pass Head pointer of the ll
    def reverseLinkedListByIteration(currentNode):
        if currentNode:
            newHead = currentNode
            currentNode = currentNode.next
            newHead.next = None
            while(currentNode is not None):
                tempNode = currentNode
                currentNode = currentNode.next
                
                tempNode.next = newHead
                newHead = tempNode
            
            while(newHead):
                print(newHead.data)
                newHead = newHead.next
    
    @staticmethod
    def reverseSingleLinkedListByReference(ll):
        if ll.head:
            tempNode = ll.head;

            ll.head = ll.head.next;
            tempNode.next = None;

            LinkedListQuestions.reverseSingleLinkedListByReference(ll);

            if ll.head is None:
                ll.head = tempNode;
                ll.tail = tempNode;
            else:
                ll.tail.next = tempNode;
                ll.tail = tempNode;

    @staticmethod
    def reverseSingleLinkedList(ll):
        LinkedListQuestions.reverseSingleLinkedListByReference(ll);
        print("\nReversed LL")
        ll.displayIterative();

    @staticmethod
    def reverseFirstKElementOfSingleLinkedListHelper(ll, size, loopCount=0):
        if ll.head:
            tempNode = ll.head;

            ll.head = ll.head.next;
#             tempNode.next = None;

            loopCount += 1;
            if loopCount < size:
                lastNode = LinkedListQuestions.reverseFirstKElementOfSingleLinkedListHelper(ll, size, loopCount);

            if loopCount == size:
                ll.head = tempNode;
                lastNode = ll.head;
            else:
                tempNode.next = lastNode.next;
                lastNode.next = tempNode;
                lastNode = tempNode;
            loopCount -= 1;
            return lastNode;

    @staticmethod
    def reverseFirstKElementOfSingleLinkedList(ll, size):
        if size == 0 or size == 1:
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
            print("\nNo Loop Found");
        
        print("\nLL After Removing the Loop")
        ll.displayIterative();

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
    def mergeTwoSortedListDecreasinglyUsingRecursionHelper(ll1Node, ll2Node, resultll):
        if ll1Node is None and ll2Node is None:
            return;
        elif ll1Node is not None and ll2Node is None:
            LinkedListQuestions.mergeTwoSortedListDecreasinglyUsingRecursionHelper(ll1Node.next, ll2Node, resultll);
            resultll.add(ll1Node.data);
            return;
        elif ll1Node is None and ll2Node is not None:
            LinkedListQuestions.mergeTwoSortedListDecreasinglyUsingRecursionHelper(ll1Node, ll2Node.next, resultll);
            resultll.add(ll2Node.data);
            return;
 
        if ll1Node.data <= ll2Node.data:
            LinkedListQuestions.mergeTwoSortedListDecreasinglyUsingRecursionHelper(ll1Node.next, ll2Node, resultll);
            resultll.add(ll1Node.data);
            return;
        else:
            LinkedListQuestions.mergeTwoSortedListDecreasinglyUsingRecursionHelper(ll1Node, ll2Node.next, resultll);
            resultll.add(ll2Node.data);
            return;

    @staticmethod
    def mergeTwoSortedListDecreasinglyUsingRecursion(ll1, ll2):
        resultll = SinglyLinkedList();
        LinkedListQuestions.mergeTwoSortedListDecreasinglyUsingRecursionHelper(ll1.head, ll2.head, resultll.head);
        print("\nmergeTwoSortedListDecreasinglyUsingRecursion")
        resultll.displayIterative();
        
    @staticmethod
    def mergeTwoSortedListDecreasinglyUsingIterationAndStack(ll1, ll2):
        resultll = SinglyLinkedList();

        ll1Node = ll1.head;
        ll2Node = ll2.head;

        stack = StackUsingLinkedList();
        
        while ll1Node is not None and ll2Node is not None:
            if ll1Node.data <= ll2Node.data:
                stack.push(ll1Node.data);
                ll1Node = ll1Node.next;
            else:
                stack.push(ll2Node.data);
                ll2Node = ll2Node.next;

        while ll1Node is not None:
            stack.push(ll1Node.data);
            ll1Node = ll1Node.next;

        while ll2Node is not None:
            stack.push(ll2Node.data);
            ll2Node = ll2Node.next;

        while stack.getSize() > 0:
            resultll.add(stack.pop());

        print("\mergeTwoSortedListDecreasinglyUsingIterationAndStack")
        resultll.displayIterative();

    @staticmethod
    def mergeTwoSortedListDecreasinglyUsingIteration(ll1, ll2):
        resultll = SinglyLinkedList();

        ll1Node = ll1.head;
        ll2Node = ll2.head;

        node = resultll.head;

        while ll1Node is not None and ll2Node is not None:
            if ll1Node.data <= ll2Node.data:
                tempNode = ll1Node.next;
                ll1Node.next = node;
                node = ll1Node;
                ll1Node = tempNode;
            else:
                tempNode = ll2Node.next;
                ll2Node.next = node;
                node = ll2Node;
                ll2Node = tempNode;

        while ll1Node is not None:
            tempNode = ll1Node.next;
            ll1Node.next = node;
            node = ll1Node;
            ll1Node = tempNode;

        while ll2Node is not None:
            tempNode = ll2Node.next;
            ll2Node.next = node;
            node = ll2Node;
            ll2Node = tempNode;
        
        resultll.head = node;

        print("\nmergeTwoSortedListDecreasinglyUsingIteration")
        resultll.displayIterative();

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
    def removeDuplicatesInUnSortedList(ll):
        LinkedListQuestions.mergeSort(ll);
        sNode = ll.head;
        LinkedListQuestions.removeDuplicatesInSortedListHelper(ll, sNode);

        print("\nUnSorted LL After Deleting Duplicate Elements");
        ll.displayIterative();

    @staticmethod
    def findMiddleNode(ll, isPrint=True):
        singleJumper = ll.head;
        doubleJumber = ll.head;

        while doubleJumber.next is not None and doubleJumber.next.next is not None:
            singleJumper = singleJumper.next;
            doubleJumber = doubleJumber.next.next;

        if isPrint:
            print("\nMiddle Node is %d " % (singleJumper.data));

        return singleJumper;

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

    @staticmethod
    def mergeHelper(fll, sll):
        result = None;

        if fll is None:
            return sll;
        elif sll is None:
            return fll;

        if (fll.data == sll.data) or (fll.data < sll.data):
            result = fll;
            result.next = LinkedListQuestions.mergeHelper(fll.next, sll);
        elif fll.data > sll.data:
            result = sll;
            result.next = LinkedListQuestions.mergeHelper(fll, sll.next);
        return result;

    @staticmethod
    def mergeSortFindMidAndSplit(sNode):
        singleJumper = sNode;
        doubleJumper = sNode;

        while doubleJumper.next is not None and doubleJumper.next.next is not None:
            singleJumper = singleJumper.next;
            doubleJumper = doubleJumper.next.next;

        fll = sNode;
        sll = singleJumper.next;
        singleJumper.next = None;
        return fll, sll;

    @staticmethod
    def mergeSortHelper(sNode):
        fll, sll = LinkedListQuestions.mergeSortFindMidAndSplit(sNode);

        if fll.next is not None:
            fll = LinkedListQuestions.mergeSortHelper(fll);
        if sll.next is not None:
            sll = LinkedListQuestions.mergeSortHelper(sll);
        return LinkedListQuestions.mergeHelper(fll, sll);

    @staticmethod
    def mergeSort(ll):
        sll = LinkedListQuestions.mergeSortHelper(ll.head)
        ll.head = sll;
        print("Sorted LL(Merge Sort)");
        ll.displayIterative();
        
    @staticmethod
    def addTwoNumberRepresentedByLLByIteration(ll1, ll2):
        carry = 0;
        ll = SinglyLinkedList();

        ll1Node = ll1.head;
        ll2Node = ll2.head;

        while ll1Node is not None and ll2Node is not None:
            total = ll1Node.data + ll2Node.data + carry;
            if total >= 10:
                carry = total / 10;
                data = total % 10;
            else:
                carry = 0;
                data = total;

            ll.add(data);

            ll1Node = ll1Node.next;
            ll2Node = ll2Node.next;

        while ll1Node is not None:
            total = ll1Node.data + carry;
            if total >= 10:
                carry = total / 10;
                data = total % 10;
            else:
                carry = 0;
                data = total;

            ll.add(data);
            ll1Node = ll1Node.next;

        while ll2Node is not None:
            total = ll2Node.data + carry;
            if total >= 10:
                carry = total / 10;
                data = total % 10;
            else:
                carry = 0;
                data = total;

            ll.add(data);
            ll2Node = ll2Node.next;
        
        if carry > 0:
            ll.add(carry);
            
        print("\nLL After Adding 2 LL By Iteration")
        ll.displayIterative();
        
    @staticmethod
    def addTwoNumberWithSameLenghtRepresentedByLLByRecursion(ll1Node, ll2Node, ll):
        if ll1Node is None:
            return 0;

        carry = LinkedListQuestions.addTwoNumberWithSameLenghtRepresentedByLLByRecursion(ll1Node.next, ll2Node.next, ll);

        total = ll1Node.data + ll2Node.data + carry;

        if total >= 10:
            carry = total / 10;
            data = total % 10;
        else:
            carry = 0;
            data = total;

        node = SinglyLinkedNode(data);

        if ll.head is None:
            ll.head = node;
            ll.tail = node;
        else:
            node.next = ll.head;
            ll.head = node;

        ll.length += 1;
        return carry;

    @staticmethod
    def addCarryToRemainingNodes(currentNode, size, carry, ll):
        if size == 0:
            return carry;

        carry = LinkedListQuestions.addCarryToRemainingNodes(currentNode.next, size - 1, carry, ll);

        total = currentNode.data + carry;

        if total >= 10:
            carry = total / 10;
            data = total % 10;
        else:
            carry = 0;
            data = total;

        node = SinglyLinkedNode(data);

        node.next = ll.head;
        ll.head = node;

        ll.length += 1;
        return carry;

#     Check For the diff in number of node count in 2 linkedlist, if 2 LL size is diff. then move the cur. pointer of larger LL till diff becomes 0. and then add them recursivelly after adding if any carry is there then add that carry to remaining nodes.
    @staticmethod
    def addTwoNumberRepresentedByLLByRecursion(ll1, ll2):
        ll1Node = ll1.head;
        ll2Node = ll2.head;

        diff = abs(ll1.size() - ll2.size());

        if ll1.size() < ll2.size():
            ll2Node = ll1.head;
            ll1Node = ll2.head;

        tempNode = ll1Node;

        while diff > 0:
            tempNode = tempNode.next;
            diff -= 1;

        ll = SinglyLinkedList();

        carry = LinkedListQuestions.addTwoNumberWithSameLenghtRepresentedByLLByRecursion(tempNode, ll2Node, ll);

        diff = abs(ll1.size() - ll2.size());

        LinkedListQuestions.addCarryToRemainingNodes(ll1Node, diff, carry, ll)

        print("\nLL After Adding 2 LL By Recursion")
        ll.displayIterative();


    @staticmethod
    def rearrangeLLHelper(currentPointer, mainPointer):
        if currentPointer is None:
            return mainPointer;

        mainPointer = LinkedListQuestions.rearrangeLLHelper(currentPointer.next, mainPointer);

        tempPointer = mainPointer.next;
        mainPointer.next = currentPointer;
        currentPointer.next = tempPointer;

        return mainPointer.next.next;

    @staticmethod
    def rearrangeLL(ll):
        middleNode = LinkedListQuestions.findMiddleNode(ll);

        tailPointer = None;
        if ll.size() & 1 == 1:  # Odd
            tailPointer = middleNode;
        else:  # Even
            tailPointer = middleNode.next;

        LinkedListQuestions.rearrangeLLHelper(middleNode.next, ll.head);

        ll.tail = tailPointer;
        ll.tail.next = None;

        print("\nLl After ReArrangement");
        ll.displayIterative();

    @staticmethod
    def cloneDoublyLLWithRandomPreviousPointerHelper(currentPointer, copydll, hashMap):
        if currentPointer is None:
            return;

        copydll.add(currentPointer.data);

#         hashMap[copydll.tail] = currentPointer;

        hashMap[copydll.tail] = copydll.tail;

        LinkedListQuestions.cloneDoublyLLWithRandomPreviousPointerHelper(currentPointer.next, copydll, hashMap);

        tPointer = hashMap[currentPointer];
        pPointer = hashMap[currentPointer.previous];
#         tPointer.previous = hashMap[currentPointer.previous];

        hashMap[currentPointer].previous = hashMap[currentPointer.previous];

    @staticmethod
    def cloneDoublyLLWithRandomPreviousPointer(dll):
        copydll = DoublyLinkedList();
        hashMap = {};

        LinkedListQuestions.cloneDoublyLLWithRandomPreviousPointerHelper(dll.head, copydll, hashMap);

        print("\n Cloned Doubly Linked list");
        copydll.displayIterative();
    
    @staticmethod
    def flattenLinkeListInSortedForm(dll):
        print();

if __name__ == '__main__':
    ll = SinglyLinkedList();
    ll.add("1");
    ll.add("2");
    ll.add("3");

    LinkedListQuestions.reverseSingleLinkedListByReference(ll)
    ll.displayIterative()
#     LinkedListQuestions.reverseSingleLinkedList(ll);

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
#     LinkedListQuestions.detectAndRemoveLoopInLinkedList(ll);
    
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
    
    
    ll1 = SinglyLinkedList();
    ll1.add(5);
    ll1.add(10);
    ll1.add(15);
    ll1.add(40);
    ll1.add(50);
    ll1.add(60);
    
    ll2 = SinglyLinkedList();
    ll2.add(2);
    ll2.add(3);
    ll2.add(20);
#     LinkedListQuestions.mergeTwoSortedListDecreasinglyUsingRecursion(ll1, ll2);
#     LinkedListQuestions.mergeTwoSortedListDecreasinglyUsingIterationAndStack(ll1, ll2);
    LinkedListQuestions.mergeTwoSortedListDecreasinglyUsingIteration(ll1, ll2);
    
    
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
    ll.add(12);
    ll.add(11);
    ll.add(12);
    ll.add(21);
    ll.add(41);
    ll.add(43);
    ll.add(21);
    LinkedListQuestions.removeDuplicatesInUnSortedList(ll);
    
    ll = SinglyLinkedList();
    ll.add(1);
    ll.add(2);
    ll.add(3);
    ll.add(4);
    ll.add(5);
    ll.add(6);
    ll.add(7);
    LinkedListQuestions.alternatingSplit(ll);

    ll = SinglyLinkedList();
    ll.add(1);
    ll.add(2);
    ll.add(3);
    ll.add(4);
    ll.add(5);
    LinkedListQuestions.reverseFirstKElementOfSingleLinkedList(ll, 2);
    print("\nLL After Reversing First " + str(4) + " Nodes");
    ll.displayIterative();
    
    
    ll = SinglyLinkedList();
    ll.add(1);
    ll.add(2);
    ll.add(3);
    ll.add(4);
    ll.add(5);
    ll.add(6);
    ll.add(7);
    ll.add(8);
    LinkedListQuestions.findMiddleNode(ll);
    
    
    ll = SinglyLinkedList();
    ll.add(6);
    ll.add(5);
    ll.add(3);
    ll.add(1);
    ll.add(8);
    ll.add(7);
    ll.add(2);
    ll.add(4);
    
    LinkedListQuestions.mergeSort(ll);


#     ll = SinglyLinkedList();
#     ll.add(6);
#     ll.add(5);
#     ll.add(3);
#     ll.add(1);
#     ll.add(8);
#     ll.add(7);
#     ll.add(2);
#     ll.add(4);
#     LinkedListQuestions.insertionSort(ll);
    
    
    ll1 = SinglyLinkedList();
    ll1.add(7)
    ll1.add(5);
    ll1.add(9);
    ll1.add(4);
    ll1.add(6);
    ll2 = SinglyLinkedList();
    ll2.add(8);
    ll2.add(4);
#     ll2.add(2);
    LinkedListQuestions.addTwoNumberRepresentedByLLByIteration(ll1, ll2);
    
    
    ll1 = SinglyLinkedList();
    ll1.add(7)
    ll1.add(5);
    ll1.add(9);
    ll1.add(4);
    ll1.add(6);
    ll2 = SinglyLinkedList();
    ll2.add(1);
    ll2.add(1);
    ll2.add(1);
    ll2.add(1);
    ll2.add(1);
    LinkedListQuestions.addTwoNumberRepresentedByLLByRecursion(ll1, ll2);
    
    ll = SinglyLinkedList();
    ll.add(1);
    ll.add(2);
    ll.add(3);
    ll.add(4);
    ll.add(5);
    ll.add(6);
    LinkedListQuestions.rearrangeLL(ll);

    dll = DoublyLinkedList();
    dll.add(1);
    dll.add(2);
    dll.add(3);
    dll.add(4);
    dll.add(5);
    dll.head.previous = dll.head.next.next;
    dll.head.next.previous = dll.head;
    dll.head.next.next.previous = dll.head.next.next.next.next;
    dll.head.next.next.next.previous = dll.head.next.next;
    dll.head.next.next.next.next.previous = dll.head.next;
    LinkedListQuestions.cloneDoublyLLWithRandomPreviousPointer(dll);
