'''
Created on 13-Jun-2016

@author: Dushyant
'''
from org.ds.queue.Queue import Queue

'''
                       20
             15                 25
        10       18        22     30
      8             19
'''

class BinarySeachTree(object):
    def __init__(self, data):
        self.left = None;
        self.right = None;
        self.data = data;

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = BinarySeachTree(data);
            else:
                self.left.insert(data);
        else:
            if self.right is None:
                self.right = BinarySeachTree(data);
            else:
                self.right.insert(data);

    def breadthFirstSearchUsingRecursionHelper(self, level):
        if level == 1:
            print(self.data);
            return;

        if self.left:
            self.left.breadthFirstSearchUsingRecursionHelper(level - 1);
        if self.right:
            self.right.breadthFirstSearchUsingRecursionHelper(level - 1);

    def breadthFirstSearchUsingRecursion(self):
        height = self.height();
        
        for iLoop in range(height + 1):
            self.breadthFirstSearchUsingRecursionHelper(iLoop);


    def breadthFirstSearchUsingQueue(self):
        queue = Queue();

        queue.enQueue(self);

        while queue.getSize() > 0:
            treeNode = queue.deQueue();

            print(treeNode.data);

            if treeNode.left:
                queue.enQueue(treeNode.left);

            if treeNode.right:
                queue.enQueue(treeNode.right);

    def depthFirstSearch(self, dfsType):
#        Pre-Order Depth First Search
        if dfsType == 1:
            if self is not None:
                print(self.data);
            if self.left is not None:
                self.left.depthFirstSearch(dfsType);
            if self.right is not None:
                self.right.depthFirstSearch(dfsType);

#         In-Order Depth First Search
        elif dfsType == 2:
            if self.left is not None:
                self.left.depthFirstSearch(dfsType);
            if self is not None:
                print(self.data);
            if self.right is not None:
                self.right.depthFirstSearch(dfsType);

#         Post-Order Depth First Search
        elif dfsType == 3:
            if self is not None and self.left is not None:
                self.left.depthFirstSearch(dfsType);
            if self.right is not None:
                self.right.depthFirstSearch(dfsType);
            if self is not None:
                print(self.data);
    
    def findMinInRightSubTree(self):
        if self is not None:
            if self.left is not None:
                return self.left.findMinInRightSubTree();
            else:
                return self.data;
        else:
            return None;

    def findMinRefInRightSubTree(self):
        if self is not None:
            if self.left is not None:
                return self.left.findMinRefInRightSubTree();
            else:
                return self;
        else:
            return None;

    def findMinInRightSubTreeAndParent(self, parent):
        if self is not None:
            if self.left is not None:
                return self.left.findMinInRightSubTreeAndParent(self);
            else:
                return self, parent;
        else:
            return None, None;

    def contains(self, data):
        if self is not None:
            if self.data == data:
                return "Present";
            elif self.data < data:
                if self.right is not None:
                    return self.right.contains(data);
                else:
                    return "ABSENT";
            elif self.data > data:
                if self.left is not None:
                    return self.left.contains(data);
                else:
                    return "ABSENT";

    def containsWithReturnRef(self, data, parent):
        if self is not None:
            if self.data == data:
                return self, parent;
            elif self.data < data:
                if self.right is not None:
                    return self.right.containsWithReturnRef(data, self);
                else:
                    return None, None;
            elif self.data > data:
                if self.left is not None:
                    return self.left.containsWithReturnRef(data, self);
                else:
                    return None, None;

    def childCount(self):
        count = 0;
        if self.left:
            count += 1;
        if self.right:
            count += 1;
        return count;

    def freeNodeMemory(self):
        self.left = None;
        self.right = None;
        del self;

    def delete(self, data):
        nodeToDelete, parentNode = self.containsWithReturnRef(data, self);
        if nodeToDelete is not None:
            count = nodeToDelete.childCount();
            if count == 0:
                if self is nodeToDelete:
                    nodeToDelete.freeNodeMemory();
                    return None;
                else:
                    if parentNode.left is nodeToDelete:
                        parentNode.left = None;
                    else:
                        parentNode.right = None;
                    return self;
            elif count == 1:
                if nodeToDelete.left:
                    child = nodeToDelete.left;
                elif nodeToDelete.right:
                    child = nodeToDelete.right;
                
                if nodeToDelete is parentNode:
                    nodeToDelete.freeNodeMemory();
                    return child;
                else:
                    if nodeToDelete.left:
                        parentNode.left = child;
                    else:
                        parentNode.right = child;
                    return  self;
            elif count == 2:
                smallestNode, smallestNodeParent = nodeToDelete.right.findMinInRightSubTreeAndParent(nodeToDelete.right);
                nodeToDelete.data = smallestNode.data;

                if smallestNode is smallestNodeParent or smallestNodeParent is nodeToDelete:
                    smallestNodeParent.right = None;
                    nodeToDelete.right = None;
                else:
                    smallestNodeParent.left = None;
                smallestNode.freeNodeMemory();
                return self;
        else:
            print("Node Not Present");
            return None;    

    def height(self):
        lheight = 0;
        rheight = 0;
        if self.left:
            lheight = self.left.height();
        if self.right:
            rheight = self.right.height();

        return (lheight + 1) if lheight > rheight else (rheight + 1);

if __name__ == '__main__':
    bst = BinarySeachTree(20);
    bst.insert(15);
    bst.insert(10);
    bst.insert(8);
    bst.insert(18);
    bst.insert(19);
    bst.insert(25);
    bst.insert(22);
    bst.insert(30);

    print("Tree Traversal(DFS)");
    bst.depthFirstSearch(2);

    print("Tree Traversal(BFS Through Recursion)");
    bst.breadthFirstSearchUsingRecursion();

    print("Tree Traversal(BFS Through Queue)");
    bst.breadthFirstSearchUsingQueue();

#     print("Height of Tree is");
#     print(bst.left.right.right.height());

    """print("Print Right Tree Min Value(Using In-order Traversal where every Time left subtree is Traversed)");
    print(BinarySeachTree.findMinInRightSubTree(bst.right));

    lowestChild, lowestChildParent = bst.right.findMinInRightSubTreeAndParent(bst.right);
    print(lowestChild.data);
    print(lowestChildParent.data);

    print("Check if Value is Present");
    print(bst.contains(2));

    childBst, parentBst = bst.containsWithReturnRef(2, bst);
    if childBst is not None and parentBst is not None:
        print(childBst.data);
        print(parentBst.data);
    else:
        print("NONE");

    print("Delete Node With Given Data");
    bst = bst.delete(20);
    print("Tree Traversal");
    if bst is not None:
        bst.depthFirstSearch(1);
    else:
        print("Empty Tree");
    """
