'''
Created on Oct 24, 2016

@author: Dushyant Sapra
'''
from org.ds.queue.Queue import Queue
from org.ds.stack.Stack import StackUsingLinkedList
from org.ds.tree.BinarySearchTree import BinarySeachTree


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
    def constructTreeUsingInorderAndPreOrderTraversalHelper(preOrderIndex, sIndex, eIndex, binaryTree, inOrderTraversal, preOrderTraversal, isLeft):
        binaryTreeNode = BinarySeachTree(preOrderTraversal[preOrderIndex]);
        if isLeft:
            binaryTree.left = binaryTreeNode;
        else:
            binaryTree.right = binaryTreeNode;

        if eIndex - sIndex == 0:
            return preOrderIndex;

        charIndex = inOrderTraversal.index(preOrderTraversal[preOrderIndex]);

        if charIndex >= sIndex:
            preOrderIndex += 1;
            preOrderIndex = BinaryTreeQuestions.constructTreeUsingInorderAndPreOrderTraversalHelper(preOrderIndex, sIndex, charIndex - 1, binaryTreeNode, inOrderTraversal, preOrderTraversal, True);

        if charIndex < eIndex:
            preOrderIndex += 1;
            preOrderIndex = BinaryTreeQuestions.constructTreeUsingInorderAndPreOrderTraversalHelper(preOrderIndex, charIndex + 1, eIndex, binaryTreeNode, inOrderTraversal, preOrderTraversal, False);

        return preOrderIndex;

    @staticmethod
    def constructTreeUsingInorderAndPreOrderTraversal(inOrderTraversal, preOrderTraversal):
        preOrderIndex = 0
        charIndex = inOrderTraversal.index(preOrderTraversal[preOrderIndex]);
        binaryTree = BinarySeachTree(preOrderTraversal[preOrderIndex]);

        preOrderIndex += 1;
        if charIndex > 0:
            BinaryTreeQuestions.constructTreeUsingInorderAndPreOrderTraversalHelper(preOrderIndex, 0, charIndex - 1, binaryTree, inOrderTraversal, preOrderTraversal, True);
        preOrderIndex = charIndex + 1;
        if charIndex < len(inOrderTraversal) - 1:
            BinaryTreeQuestions.constructTreeUsingInorderAndPreOrderTraversalHelper(preOrderIndex, charIndex + 1, len(inOrderTraversal) - 1, binaryTree, inOrderTraversal, preOrderTraversal, False);

        print("Constructed Binary Tree Using Inorder and Preorder Traversal is ");
        binaryTree.depthFirstSearch(1);
    
    
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
    def checkIfTreeIsSubTreeOfMainTree(mainTree, subTree):
        print()

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
    
#     BinaryTreeQuestions.constructTreeUsingInorderAndPreOrderTraversal(["D", "B", "E", "A", "F", "C"], ["A", "B", "D", "E", "C", "F"]);

#     BinaryTreeQuestions.constructTreeUsingInorderAndPreOrderTraversal([6, 8, 9, 10, 13, 15, 18, 20, 28, 30, 33, 35, 37, 38], [20, 10, 8, 6, 9, 15, 13, 18, 35, 30, 28, 33, 38, 37]);

#     BinaryTreeQuestions.constructTreeUsingInorderAndPreOrderTraversal([6, 8, 9, 10, 13, 15, 18, 20], [20, 10, 8, 6, 9, 15, 13, 18]);

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
