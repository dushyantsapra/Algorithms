'''
Created on Oct 24, 2016

@author: Dushyant Sapra
'''
from org.ds.queue.Queue import Queue
from org.ds.stack.Stack import StackUsingLinkedList
from org.ds.tree.BinarySearchTree import BinarySeachTree
from compiler.ast import Node
from calendar import isleap


class BinaryTreeQuestions:
    @staticmethod
    def findSizeHelper(binaryTree):
        if binaryTree is None:
            return 0;

        leftSize = BinaryTreeQuestions.findSizeHelper(binaryTree.left);
        rightSize = BinaryTreeQuestions.findSizeHelper(binaryTree.right);

        return leftSize + rightSize + 1;

    @staticmethod
    def findSize(binaryTree):
        binaryTreeSize = BinaryTreeQuestions.findSizeHelper(binaryTree);

        print("Size of Tree is " + str(binaryTreeSize));
    
    @staticmethod
    def checkIfTwoTreeAreIdenticalHelper(binaryTree1, binaryTree2):
        if binaryTree1 is None and binaryTree2 is None:
            return True;

        if binaryTree1 is not None and binaryTree2 is not None:
            if binaryTree1.data == binaryTree2.data and BinaryTreeQuestions.checkIfTwoTreeAreIdenticalHelper(binaryTree1.left, binaryTree2.left) and BinaryTreeQuestions.checkIfTwoTreeAreIdenticalHelper(binaryTree1.right, binaryTree2.right):
                return True;
            else:
                return False;
        else:
            return False;

    @staticmethod
    def checkIfTwoTreeAreIdentical(binaryTree1, binaryTree2):
        if BinaryTreeQuestions.checkIfTwoTreeAreIdenticalHelper(binaryTree1, binaryTree2):
            print("Given Tree's are Identical");
        else:
            print("Given Tree's are not Identical");

    @staticmethod
    def deleteTree(binaryTree):
        if binaryTree is None:
            return None;

        binaryTree.left = BinaryTreeQuestions.deleteTree(binaryTree.left);
        binaryTree.right = BinaryTreeQuestions.deleteTree(binaryTree.right);

        del binaryTree;
        return None;

    @staticmethod
    def convertTreeIntoMirrorTreeHelper(binaryTree):
        if binaryTree.left:
            BinaryTreeQuestions.convertTreeIntoMirrorTreeHelper(binaryTree.left);
        if binaryTree.right:
            BinaryTreeQuestions.convertTreeIntoMirrorTreeHelper(binaryTree.right);

        binaryTree.left, binaryTree.right = binaryTree.right, binaryTree.left;

    @staticmethod
    def convertTreeIntoMirrorTree(binaryTree):
        print("Original Tree");
        binaryTree.depthFirstSearch(1);
        BinaryTreeQuestions.convertTreeIntoMirrorTreeHelper(binaryTree);
        print("Mirror Tree");
        binaryTree.depthFirstSearch(1);

    @staticmethod
    def printAllPathHelper(binaryTree, queue):
        if binaryTree.left is None and binaryTree.right is None:
            queue.append(binaryTree.data);
            print(queue);
            queue.pop();

        queue.append(binaryTree.data);

        if binaryTree.left:
            BinaryTreeQuestions.printAllPathHelper(binaryTree.left, queue);
        if binaryTree.right:
            BinaryTreeQuestions.printAllPathHelper(binaryTree.right, queue);

        queue.pop();

    @staticmethod
    def printAllPath(binaryTree):
        queue = [];
        BinaryTreeQuestions.printAllPathHelper(binaryTree, queue);

    @staticmethod
    def checkIfTreeHasSumPropertyHelper(binaryTree):
        if binaryTree.left is None and binaryTree.right is None:
            return True;

        isLeftTrue = True;
        isRightTrue = True;

        leftNodeData = 0;
        rightNodeData = 0;

        if binaryTree.left:
            isLeftTrue = BinaryTreeQuestions.checkIfTreeHasSumPropertyHelper(binaryTree.left);
            leftNodeData = binaryTree.left.data;
        if binaryTree.right:
            isRightTrue = BinaryTreeQuestions.checkIfTreeHasSumPropertyHelper(binaryTree.right);
            rightNodeData = binaryTree.right.data;

        if (isLeftTrue and isRightTrue) and (binaryTree.data == leftNodeData + rightNodeData):
            return True;
        else:
            return False;

#     For every node, data value must be equal to sum of data values in left and right children.
    @staticmethod
    def checkIfTreeHasSumProperty(binaryTree):
        if BinaryTreeQuestions.checkIfTreeHasSumPropertyHelper(binaryTree):
            print("Every Tree Node Follows Sum Property");
        else:
            print("Tree Doesn't follow Sum Property");

    @staticmethod
    def checkAndMakeTreeFollowSumPropertyHelper(binaryTree):
        if binaryTree.left is None and binaryTree.right is None:
            return True;

        isLeftTrue = True;
        isRightTrue = True;

        leftNodeData = 0;
        rightNodeData = 0;

        if binaryTree.left:
            isLeftTrue = BinaryTreeQuestions.checkAndMakeTreeFollowSumPropertyHelper(binaryTree.left);
            leftNodeData = binaryTree.left.data;
        if binaryTree.right:
            isRightTrue = BinaryTreeQuestions.checkAndMakeTreeFollowSumPropertyHelper(binaryTree.right);
            rightNodeData = binaryTree.right.data;

        if (isLeftTrue and isRightTrue) and (binaryTree.data == leftNodeData + rightNodeData):
            return True;
        else:
            binaryTree.data = leftNodeData + rightNodeData
            return False;

    @staticmethod
    def checkAndMakeTreeFollowSumProperty(binaryTree):
        print("checkAndMakeTreeFollowSumProperty");
        print("Original Tree is ");
        binaryTree.depthFirstSearch(2);
        BinaryTreeQuestions.checkAndMakeTreeFollowSumPropertyHelper(binaryTree);
        print("Tree with Sum Property ");
        binaryTree.depthFirstSearch(2);

    @staticmethod
    def findHeightUsingIteration(binaryTree):
        queue = Queue();

        queue.enQueue(binaryTree);

        height = 0;

        while True:
            currentCount = queue.getSize();
            if currentCount == 0:
                break;

            height += 1;

            while currentCount > 0:
                node = queue.deQueue();

                if node.left:
                    queue.enQueue(node.left);
    
                if node.right:
                    queue.enQueue(node.right);
    
                currentCount -= 1;

        print("Tree Height Using Iteration " + str(height));

    @staticmethod
    def sortAnArrayUsingBinaryTree(arr):
        binaryTree = BinarySeachTree(arr[0]);
        length = len(arr);
        for iLoop in range(1, length):
            binaryTree.insert(arr[iLoop]);

        print("Sorted Array is ");
        binaryTree.depthFirstSearch(2);

    @staticmethod
    def constructTreeUsingInorderAndPreOrderTraversalHelper(preIndex, inOrderTraversal, preOrderTraversal, sIndex, eIndex):
        binaryTree = BinarySeachTree(preOrderTraversal[preIndex]);

        if eIndex - sIndex == 0:
            return binaryTree, preIndex;

        charIndex = inOrderTraversal.index(preOrderTraversal[preIndex]);

        index = preIndex;
        if charIndex > sIndex:
            binaryTree.left, index = BinaryTreeQuestions.constructTreeUsingInorderAndPreOrderTraversalHelper(preIndex + 1, inOrderTraversal, preOrderTraversal, sIndex, charIndex - 1);

        index += 1;

        if charIndex < eIndex:
            binaryTree.right, index = BinaryTreeQuestions.constructTreeUsingInorderAndPreOrderTraversalHelper(index, inOrderTraversal, preOrderTraversal, charIndex + 1, eIndex);

        return binaryTree, index;

    @staticmethod
    def constructTreeUsingInorderAndPreOrderTraversal(inOrderTraversal, preOrderTraversal):
        binaryTree, index = BinaryTreeQuestions.constructTreeUsingInorderAndPreOrderTraversalHelper(0, inOrderTraversal, preOrderTraversal, 0, len(inOrderTraversal) - 1);

        print("Constructed Binary Tree Using Inorder and Preorder Traversal is ");
        binaryTree.depthFirstSearch(2);
    
    @staticmethod 
    def postOrderTraversalUsingTwoStack(binaryTree):
        stack1 = StackUsingLinkedList();
        stack2 = StackUsingLinkedList();

        stack1.push(binaryTree);

        while stack1.getTop():
            headNode = stack1.pop();

            stack2.push(headNode);

            if headNode.left:
                stack1.push(headNode.left);

            if headNode.right:
                stack1.push(headNode.right);

        print("Post Order Traversal using 2 Stacks");
        while stack2.getTop():
            node = stack2.pop();
            print(node.data);

    @staticmethod
    def postOrderTraversalUsingOneStack(binaryTree):
        print();

    @staticmethod
    def constructFullBinaryTreeUsingPreOrderAndPostOrderTraversalHelper(preOrderIndex, preOrderTraversal, postOrderTraversal, sIndex, eIndex):
        node = BinarySeachTree(preOrderTraversal[preOrderIndex]);

        if sIndex == eIndex:
            return node, preOrderIndex;

        if (preOrderIndex + 1) == len(postOrderTraversal):
            return node, preOrderIndex,
        
        newIndex = postOrderTraversal.index(preOrderTraversal[preOrderIndex + 1]);

        if newIndex > eIndex:
            return node, preOrderIndex;

        index = preOrderIndex;

        if newIndex == sIndex:
            node.left, index = BinaryTreeQuestions.constructFullBinaryTreeUsingPreOrderAndPostOrderTraversalHelper(index + 1, preOrderTraversal, postOrderTraversal, sIndex, newIndex);
            node.right, index = BinaryTreeQuestions.constructFullBinaryTreeUsingPreOrderAndPostOrderTraversalHelper(index + 1, preOrderTraversal, postOrderTraversal, newIndex + 1, eIndex);
        else:
            node.left, index = BinaryTreeQuestions.constructFullBinaryTreeUsingPreOrderAndPostOrderTraversalHelper(index + 1, preOrderTraversal, postOrderTraversal, sIndex, newIndex - 1);
            node.right, index = BinaryTreeQuestions.constructFullBinaryTreeUsingPreOrderAndPostOrderTraversalHelper(index + 1, preOrderTraversal, postOrderTraversal, newIndex + 1, eIndex);

        return node, index;

    @staticmethod
    def constructFullBinaryTreeUsingPreOrderAndPostOrderTraversal(preOrderTraversal, postOrderTraversal):
        binaryTree, index = BinaryTreeQuestions.constructFullBinaryTreeUsingPreOrderAndPostOrderTraversalHelper(0, preOrderTraversal, postOrderTraversal, 0, len(postOrderTraversal) - 1);

        print("Constructed Full Binary Tree Using Preorder and postorder Traversal is ");
        binaryTree.depthFirstSearch(3);
    
    @staticmethod
    def printLevelOrderTraversalInSpiralFormUsingStack(binaryTree):
        isLeftToRight = False;

        stack = StackUsingLinkedList();

        stack.push(binaryTree);

        print("Level Order Traversal in Spiral Form is");
        while stack.getTop():
            currentLevelSize = stack.getSize();

            tempStack = StackUsingLinkedList();
            while currentLevelSize > 0:
                currentNode = stack.pop();
                print(currentNode.data);
                currentLevelSize -= 1;

                if isLeftToRight:
                    if currentNode.left:
                        tempStack.push(currentNode.left);
                    if currentNode.right:
                        tempStack.push(currentNode.right);
                else:
                    if currentNode.right:
                        tempStack.push(currentNode.right);
                    if currentNode.left:
                        tempStack.push(currentNode.left);
            stack = tempStack;

            if isLeftToRight:
                isLeftToRight = False;
            else:
                isLeftToRight = True;

    @staticmethod
    def printLevelOrderInReverseOrderHelper(binaryTreeNode, level):
        if level == 1:
            print(binaryTreeNode.data);
            return;

        if binaryTreeNode.left:
            BinaryTreeQuestions.printLevelOrderInReverseOrderHelper(binaryTreeNode.left, level - 1);

        if binaryTreeNode.right:
            BinaryTreeQuestions.printLevelOrderInReverseOrderHelper(binaryTreeNode.right, level - 1);

    @staticmethod
    def printLevelOrderInReverseOrder(binaryTree):
        height = binaryTree.height();

        print("Level Order Traversal In Reverse Order is");
        for iLoop in reversed(range(height + 1)):
            BinaryTreeQuestions.printLevelOrderInReverseOrderHelper(binaryTree, iLoop);

    @staticmethod
    def preOrderTraversalUsingSingleStack(binaryTree):
        stack = StackUsingLinkedList();
        
        stack.push(binaryTree);
        
        print("Pre Order Traversal Using Single Stack is ");

        while stack.getTop():
            node = stack.pop();
            
            print(node.data);
            
            if node.right:
                stack.push(node.right);
            
            if node.left:
                stack.push(node.left);

    @staticmethod
    def inOrderTraversalUsingStack(binaryTree):
        isDone = False;

        stack = StackUsingLinkedList();
        stack.push(binaryTree);

        current = binaryTree;

        print("InOrder Traversal Using Stack");

        while not isDone:
            if current is not None and current.left:
                stack.push(current.left);
                current = current.left;
            else:
                current = stack.pop();
                print(current.data);

                if current.right:
                    stack.push(current.right);
                    current = current.right;
                else:
                    if stack.getSize() == 0:
                        break;
                    current = None;

    @staticmethod
    def postOrderTraversalUsingSingleStack(binaryTree):
        currentNode = binaryTree;

        stack = StackUsingLinkedList();

        print("Post Order Traversal Using Single Stack");
        while True:
            if currentNode:
                if currentNode.right:
                    stack.push(currentNode.right);
                stack.push(currentNode);
                currentNode = currentNode.left;
            else:
                if stack.getTop():
                    node = stack.pop();

                    if node.right and node.right is stack.getTop():
                        currentNode = stack.pop();
                        stack.push(node);
                    else:
                        print(node.data);
                else:
                    break;

    @staticmethod
    def updateTreeWithLeftTreeSumHelper(binaryTreeNode, isLeft):
        lSum = 0;
        rSum = 0;

        if binaryTreeNode.left:
            lSum = BinaryTreeQuestions.updateTreeWithLeftTreeSumHelper(binaryTreeNode.left, isLeft);

        if binaryTreeNode.right:
            rSum = BinaryTreeQuestions.updateTreeWithLeftTreeSumHelper(binaryTreeNode.right, False);

        if isLeft:
            binaryTreeNode.data += lSum;
            return binaryTreeNode.data + rSum;
        else:
            return binaryTreeNode.data + lSum + rSum;

#     Change a Binary Tree so that every node stores sum of all nodes in left subtree
    @staticmethod
    def updateTreeWithLeftTreeSum(binaryTree):
        if binaryTree.left:
            binaryTree.data += BinaryTreeQuestions.updateTreeWithLeftTreeSumHelper(binaryTree.left, True);

        print("updateTreeWithLeftTreeSum is ");
        binaryTree.depthFirstSearch(1);

if __name__ == '__main__':
    binaryTree = BinarySeachTree(1);
    binaryTree.left = BinarySeachTree(2);
    binaryTree.right = BinarySeachTree(3);

    binaryTree.left.left = BinarySeachTree(4);
    binaryTree.left.right = BinarySeachTree(5);
    binaryTree.right.left = BinarySeachTree(6);
    binaryTree.right.right = BinarySeachTree(7);

    BinaryTreeQuestions.findSize(binaryTree);
    
    bst = BinarySeachTree(20);
    bst.insert(15);
    bst.insert(10);
    bst.insert(8);
    bst.insert(18);
    bst.insert(19);
    bst.insert(25);
    bst.insert(22);
    bst.insert(30);
    BinaryTreeQuestions.inOrderTraversalUsingStack(bst);
    
    bst1 = BinarySeachTree(20);
    bst1.insert(15);
    bst1.insert(10);
    bst1.insert(8);
    bst1.insert(18);
    bst1.insert(19);
    bst1.insert(25);
    bst1.insert(22);
    bst1.insert(30);
    
    bst2 = BinarySeachTree(20);
    bst2.insert(15);
    bst2.insert(10);
    bst2.insert(8);
    bst2.insert(18);
    bst2.insert(19);
    bst2.insert(25);
    bst2.insert(22);
    bst2.insert(30);
    BinaryTreeQuestions.checkIfTwoTreeAreIdentical(bst1, bst2);
    
    bst = BinarySeachTree(20);
    bst.insert(15);
    bst.insert(10);
    bst.insert(8);
    bst.insert(18);
    bst.insert(19);
    bst.insert(25);
    bst.insert(22);
    bst.insert(30);
    BinaryTreeQuestions.deleteTree(bst);
    
    binaryTree = BinarySeachTree(1);
    binaryTree.left = BinarySeachTree(2);
    binaryTree.right = BinarySeachTree(3);

    binaryTree.left.left = BinarySeachTree(4);
    binaryTree.left.right = BinarySeachTree(5);
    binaryTree.right.left = BinarySeachTree(6);
    binaryTree.right.right = BinarySeachTree(7);
    BinaryTreeQuestions.convertTreeIntoMirrorTree(binaryTree);
    
    
    binaryTree = BinarySeachTree(1);
    binaryTree.left = BinarySeachTree(2);
    binaryTree.right = BinarySeachTree(3);

    binaryTree.left.left = BinarySeachTree(4);
    binaryTree.left.right = BinarySeachTree(5);
    binaryTree.right.left = BinarySeachTree(6);
    binaryTree.right.right = BinarySeachTree(7);
    BinaryTreeQuestions.printAllPath(binaryTree);
    
    
    binaryTree = BinarySeachTree(10);
    binaryTree.left = BinarySeachTree(8);
    binaryTree.right = BinarySeachTree(2);

    binaryTree.left.left = BinarySeachTree(3);
    binaryTree.left.right = BinarySeachTree(5);
    binaryTree.right.left = BinarySeachTree(2);
    BinaryTreeQuestions.checkIfTreeHasSumProperty(binaryTree);


    binaryTree = BinarySeachTree(10);
    binaryTree.left = BinarySeachTree(7);
    binaryTree.right = BinarySeachTree(2);
    binaryTree.left.left = BinarySeachTree(3);
    binaryTree.left.right = BinarySeachTree(5);
    binaryTree.right.left = BinarySeachTree(5);
    BinaryTreeQuestions.checkAndMakeTreeFollowSumProperty(binaryTree);
    
    BinaryTreeQuestions.constructTreeUsingInorderAndPreOrderTraversal(["D", "B", "E", "A", "F", "C"], ["A", "B", "D", "E", "C", "F"]);
 
    BinaryTreeQuestions.constructTreeUsingInorderAndPreOrderTraversal([6, 8, 9, 10, 13, 15, 18, 20, 28, 30, 33, 35, 37, 38], [20, 10, 8, 6, 9, 15, 13, 18, 35, 30, 28, 33, 38, 37]);
 
    BinaryTreeQuestions.constructTreeUsingInorderAndPreOrderTraversal([6, 8, 9, 10, 13, 15, 18, 20], [20, 10, 8, 6, 9, 15, 13, 18]);

    BinaryTreeQuestions.constructTreeUsingInorderAndPreOrderTraversal([20], [20]);
    
    bst = BinarySeachTree(20);
    bst.insert(10);
    bst.insert(35);
    bst.insert(8);
    bst.insert(18);
    bst.insert(30);
    bst.insert(40);
    bst.insert(7);
    bst.insert(9);
    bst.insert(15);
    bst.insert(19);
    BinaryTreeQuestions.findHeightUsingIteration(bst);
    
    BinaryTreeQuestions.sortAnArrayUsingBinaryTree([-1, 15, 10, 25, 5, 50, 11, 18, 9, 2]);
    BinaryTreeQuestions.sortAnArrayUsingBinaryTree([15, 10, 25, 5, 11, 20]);
    
#     BinaryTreeQuestions.constructTreeUsingInorderAndPreOrderTraversalNew([4, 5, 8, 10, 12, 15, 18, 20, 25, 30, 35], [20, 10, 5, 4, 8, 15, 12, 18, 30, 25, 35]);
#     BinaryTreeQuestions.constructTreeUsingInorderAndPreOrderTraversalNew([6, 8, 9, 10, 13, 15, 18, 20, 28, 30, 33, 35, 37, 38], [20, 10, 8, 6, 9, 15, 13, 18, 35, 30, 28, 33, 38, 37]);
#     BinaryTreeQuestions.constructTreeUsingInorderAndPreOrderTraversalNew([8, 10, 15, 20, 30, 35], [20, 10, 8, 15, 35, 30]);

    bst = BinarySeachTree(20);
    bst.insert(10);
    bst.insert(35);
    bst.insert(8);
    bst.insert(18);
    bst.insert(30);
    bst.insert(40);
    bst.insert(7);
    bst.insert(9);
    bst.insert(15);
    bst.insert(19);
    BinaryTreeQuestions.postOrderTraversalUsingTwoStack(bst);

#     BinaryTreeQuestions.constructFullBinaryTreeUsingPreOrderAndPostOrderTraversal([20, 10, 8, 7, 9, 18, 15, 19, 35, 30, 40], [7, 9, 8, 15, 19, 18, 10, 30, 40, 35, 20]);
#     BinaryTreeQuestions.constructFullBinaryTreeUsingPreOrderAndPostOrderTraversal([20, 10, 8, 7, 9, 18, 35], [7, 9, 8, 18, 10, 35, 20]);

    BinaryTreeQuestions.constructFullBinaryTreeUsingPreOrderAndPostOrderTraversal([20, 10, 8, 15, 35, 30, 25, 32, 40], [8, 15, 10, 25, 32, 30, 40, 35, 20]);
    
    bst = BinarySeachTree(20);
    bst.insert(10);
    bst.insert(35);
    bst.insert(5);
    bst.insert(18);
    bst.insert(30);
    bst.insert(40);
    bst.insert(45);
    bst.insert(42);
    bst.insert(48);
    bst.insert(6);
    bst.insert(9);
    bst.insert(15);
    bst.insert(19);
    bst.insert(4);
    bst.insert(8);

#     print("Test")
#     bst.depthFirstSearch(1);

    BinaryTreeQuestions.printLevelOrderTraversalInSpiralFormUsingStack(bst);
    
    bst = BinarySeachTree(20);
    bst.insert(10);
    bst.insert(35);
    bst.insert(8);
    bst.insert(12);
    bst.insert(2);
    bst.insert(9);
    bst.insert(11);
    bst.insert(15);
    bst.insert(28);
    bst.insert(40);
    
#     print("Hello");
#     bst.depthFirstSearch(1);
    BinaryTreeQuestions.printLevelOrderInReverseOrder(bst);
    
    
    bst = BinarySeachTree(20);
    bst.insert(10);
    bst.insert(35);
    bst.insert(5);
    bst.insert(18);
    bst.insert(30);
    bst.insert(40);
    bst.insert(45);
    bst.insert(42);
    bst.insert(48);
    bst.insert(6);
    bst.insert(9);
    bst.insert(15);
    bst.insert(19);
    bst.insert(4);
    bst.insert(2);
    bst.insert(3);
    bst.insert(1);
    bst.insert(8);
    BinaryTreeQuestions.preOrderTraversalUsingSingleStack(bst);
    
    BinaryTreeQuestions.postOrderTraversalUsingSingleStack(bst);
    
    BinaryTreeQuestions.updateTreeWithLeftTreeSum(bst);
