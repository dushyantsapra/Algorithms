'''
Created on 23-Jun-2016

@author: Dushyant Sapra
'''

'''
    Not Working Yet, Single case is messing Up, Will solve it when time permits.
'''

'''
    Rules for RedBlack Tree
        1. Root is Always Black
        2. No Red Red Parent Child Relationship
        3. Number of black nodes from root to node with less then 2 children's is same.

   Rules for Insertion into RedBlack Tree
        1. if tree is empty create black root node.
        2. Insert new leaf node as red:
            i) if parent is black then done.
            ii) if parent is red:
                a) if parent sibling is black or absent rotate, re-color and done
                b) if parent sibling is red then re-color and check again.
'''

class RedBlackTree:
    def __init__(self, data, parent, color):
        self.data = data;
        self.parent = parent;
        self.color = color;
        self.left = None;
        self.right = None;

    def rightRotate(self):
        newNode = self.left;
        self.left = None;
        self.left = newNode.right;
        newNode.right.parent = self.left;
        newNode.right = self;

        newNode.parent = self.parent;
        self.parent = newNode;

        return newNode;

    def leftRotate(self):
        newNode = self.right;
        self.right = None;
        self.right = newNode.left;
        newNode.left.parent = self.right;
        newNode.left = self;

        newNode.parent = self.parent;
        self.parent = newNode;

        return newNode;
    
    def rightRotateWithReColor(self, isRecolor):
        newNode = self.left;
        self.left = None;
        self.left = newNode.right;
        newNode.right.parent = self.left;
        newNode.right = self;

        newNode.parent = self.parent;
        self.parent = newNode;

        if newNode.parent:
            if newNode.parent.data > newNode.data:
                newNode.parent.left = newNode;
            else:
                newNode.parent.right = newNode;

        if isRecolor:
            newNode.right.color = "RED";
            newNode.color = "BLACK";

        return newNode;

    def leftRotateWithReColor(self, isRecolor):
        newNode = self.right;
        self.right = None;
        self.right = newNode.left;
        newNode.left.parent = self.right;
        newNode.left = self;

        newNode.parent = self.parent;
        self.parent = newNode;

        if newNode.parent:
            if newNode.parent.data > newNode.data:
                newNode.parent.left = newNode;
            else:
                newNode.parent.right = newNode;

        if isRecolor:
            newNode.left.color = "RED";
            newNode.color = "BLACK";

        return newNode;

    def reArrgangeAndReColor(self, gpToParent, parentToChild):
#         Left Left Case
        if gpToParent is "LEFT" and parentToChild is "LEFT":
#             Right Rotation
            self = self.rightRotate();

#             Recoloring
            self.color = "BLACK";
            self.right.color = "RED";
            
            return self;
#         Left Right Case
        if gpToParent is "LEFT" and parentToChild is "RIGHT":
#             Left Rotation
            self.left = self.left.leftRotate();
            
#             Right Rotation
            self = self.rightRotate();

#             Recoloring
            self.color = "BLACK";
            self.right.color = "RED";

            return self;
#         Right Right Case
        if gpToParent is "RIGHT" and parentToChild is "RIGHT":
#             Left Rotation
            self = self.leftRotate();

#             Recoloring
            self.color = "BLACK";
            self.left.color = "RED";

            return self;
#         Right Left Case
        if gpToParent is "RIGHT" and parentToChild is "LEFT":
#             Right Rotation
            self.right = self.right.rightRotate();
            
#             Left Rotation
            self = self.leftRotate();

#             Recoloring
            self.color = "BLACK";
            self.left.color = "RED";

            return self;

    def reColor(self):
        self.right.color = "BLACK";
        self.left.color = "BLACK";
        if self.parent:
            self.color = "RED";
        return self;

    def restoreBalance(self, gpToParent, parentToChild):
        if gpToParent is "LEFT":
            if self.right is None or self.right is "BLACK":
                self = self.reArrgangeAndReColor(gpToParent, parentToChild);
            else:
                self = self.reColor();
        else:
            if self.left is None or self.left is "BLACK":
                self = self.reArrgangeAndReColor(gpToParent, parentToChild);
            else:
                self = self.reColor();
        return self;

    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = RedBlackTree(data, self, "RED");
                return self;
            else:
                self.left = self.left.insert(data);
                if self.color is self.left.color and self.color is "RED":
                    return self;
                else:
                    if data < self.left.data:
                        if self.left.color is self.left.left.color and self.left.color is "RED":
                            self = self.restoreBalance("LEFT", "LEFT");
                    else:
                        if self.left.color is self.left.right.color and self.left.color is "RED":
                            self = self.restoreBalance("LEFT", "RIGHT");
                    return self;
        else:
            if self.right is None:
                self.right = RedBlackTree(data, self, "RED");
                return self;
            else:
                self.right = self.right.insert(data);
                if self.color is self.right.color and self.color is "RED":
                    return self;
                else:
                    if data > self.right.data:
                        if self.right.color is self.right.right.color and self.right.color is "RED":
                            self = self.restoreBalance("RIGHT", "RIGHT");
                    else:
                        if self.right.color is self.right.left.color and self.right.color is "RED":
                            self = self.restoreBalance("RIGHT", "LEFT");
                    return self;

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

    def childCount(self):
        count = 0;
        if self.left:
            count += 1;
        if self.right:
            count += 1;
        return count;

    def containsWithReturnRef(self, data):
        if self is not None:
            if self.data == data:
                return self;
            elif self.data < data:
                if self.right is not None:
                    return self.right.containsWithReturnRef(data);
                else:
                    return None;
            elif self.data > data:
                if self.left is not None:
                    return self.left.containsWithReturnRef(data);
                else:
                    return None;

    def findMinRefInRightSubTree(self):
        if self:
            if self.left:
                return self.left.findMinRefInRightSubTree();
            else:
                return self;
        else:
            return None;

    def freeNodeMemory(self):
        self.left = None;
        self.right = None;
        self.color = None;
        del self;
        
    def findMinNode(self):
        if self.left:
            return self.left.findMinNode();
        else:
            return self;

    def checkAndDeleteCase1(self, rootNode, doubleBlackNode):
        if doubleBlackNode.parent is None:
            doubleBlackNode.color = "BLACK";
            return rootNode;
        else:
            return rootNode.checkAndDeleteCase2(rootNode, doubleBlackNode);

    def checkAndDeleteCase2(self, rootNode, doubleBlackNode):
        if doubleBlackNode.parent.left and doubleBlackNode.parent.left is doubleBlackNode:
            if doubleBlackNode.parent.right.color is "RED" and doubleBlackNode.parent.color is "BLACK":
                # Left Rotation
                if doubleBlackNode.parent.parent:
                    doubleBlackNode.parent.leftRotateWithReColor(True);
                else:
                    rootNode = doubleBlackNode.parent.leftRotateWithReColor(True);
        else:
            if doubleBlackNode.parent.left.color is "RED" and doubleBlackNode.parent.color is "BLACK":
                # Right Rotation
                if doubleBlackNode.parent.parent:
                    doubleBlackNode.parent.rightRotateWithReColor(True);
                else:
                    rootNode = doubleBlackNode.parent.rightRotateWithReColor(True);
        return rootNode.checkAndDeleteCase3(rootNode, doubleBlackNode);

    def checkAndDeleteCase3(self, rootNode, doubleBlackNode):
        isTrue = False;
        if doubleBlackNode.parent.left and doubleBlackNode.parent.left is doubleBlackNode:
            if doubleBlackNode.parent.right.color is "BLACK" and doubleBlackNode.parent.color is "BLACK" and (doubleBlackNode.parent.right.childCount() == 0 or (doubleBlackNode.parent.right.right.color is "BLACK" and doubleBlackNode.parent.right.left.color is "BLACK")):
                doubleBlackNode.parent.right.color = "RED"
                isTrue = True;
        else:
            if doubleBlackNode.parent.left.color is "BLACK" and doubleBlackNode.parent.color is "BLACK" and (doubleBlackNode.parent.left.childCount() == 0 or (doubleBlackNode.parent.left.left.color is "BLACK" and doubleBlackNode.parent.left.right.color is "BLACK")):
                doubleBlackNode.parent.left.color = "RED"
                isTrue = True;
        if isTrue:
            return rootNode.checkAndDeleteCase1(rootNode, doubleBlackNode.parent);
        else:
            return rootNode.checkAndDeleteCase4(rootNode, doubleBlackNode);

    def checkAndDeleteCase4(self, rootNode, doubleBlackNode):
        if doubleBlackNode.parent.left and doubleBlackNode.parent.left is doubleBlackNode:
            if doubleBlackNode.parent.right.color is "BLACK" and doubleBlackNode.parent.color is "RED":
                doubleBlackNode.parent.color = "BLACK";
                doubleBlackNode.parent.right.color = "RED";
                return rootNode;
        else:
            if doubleBlackNode.parent.left.color is "BLACK" and doubleBlackNode.parent.color is "RED":
                doubleBlackNode.parent.color = "BLACK";
                doubleBlackNode.parent.left.color = "RED";
                return rootNode;
        return rootNode.checkAndDeleteCase5(rootNode, doubleBlackNode);

    def checkAndDeleteCase5(self, rootNode, doubleBlackNode):
        if doubleBlackNode.parent.left and doubleBlackNode.parent.left is doubleBlackNode:
            if doubleBlackNode.parent.right.color is "BLACK" and doubleBlackNode.parent.color is "BLACK" and doubleBlackNode.parent.right.right and doubleBlackNode.parent.right.right.color is "BLACK" and doubleBlackNode.parent.right.left and doubleBlackNode.parent.right.left.color is "RED":
                doubleBlackNode.parent.right.rightRotateWithReColor(True);
        else:
            if doubleBlackNode.parent.left.color is "BLACK" and doubleBlackNode.parent.color is "BLACK" and doubleBlackNode.parent.left.left and doubleBlackNode.parent.left.left.color is "BLACK" and doubleBlackNode.parent.left.right and doubleBlackNode.parent.left.right.color is "RED":
                doubleBlackNode.parent.left.leftRotateWithReColor(True);
        return rootNode.checkAndDeleteCase6(rootNode, doubleBlackNode);

    def checkAndDeleteCase6(self, rootNode, doubleBlackNode):
        if doubleBlackNode.parent.left and doubleBlackNode.parent.left is doubleBlackNode:
            if doubleBlackNode.parent.right.color is "BLACK" and doubleBlackNode.parent.right.right.color is "RED":
                tempColor = doubleBlackNode.parent.color;
                if doubleBlackNode.parent.parent:
                    tempNode = doubleBlackNode.parent.leftRotate();
                    tempNode.color = tempColor;
                    tempNode.left.color = tempNode.right.color = "BLACK"; 
                else:
                    rootNode = doubleBlackNode.parent.leftRotate();
                    rootNode.color = tempColor;
                    rootNode.left.color = rootNode.right.color = "BLACK";
        else:
            if doubleBlackNode.parent.left.color is "BLACK" and doubleBlackNode.parent.left.left.color is "RED":
                tempColor = doubleBlackNode.parent.color;
                if doubleBlackNode.parent.parent:
                    tempNode = doubleBlackNode.parent.rightRotate();
                    tempNode.color = tempColor;
                    tempNode.left.color = tempNode.right.color = "BLACK"; 
                else:
                    rootNode = doubleBlackNode.parent.rightRotate();
                    rootNode.color = tempColor;
                    rootNode.left.color = rootNode.right.color = "BLACK";

        return rootNode;

    def deleteHelper(self, rootNode, data):
        if self.data == data:
            childCount = self.childCount();
            if childCount == 2:
                minNode = self.right.findMinNode();
                self.data = minNode.data;
                return self.right.deleteHelper(rootNode, minNode.data);
            elif childCount == 1:
                print("Parking This Case For Now");        
            else:
                if self.color is "RED":
                    if self.parent.left and self.parent.left is self:
                        self.parent.left = None;
                    else:
                        self.parent.right = None;
                else:
                    rootNode = rootNode.checkAndDeleteCase1(rootNode, self);
                    if self.parent.left and self.parent.left is self:
                        self.parent.left = None;
                    else:
                        self.parent.right = None;
                    return rootNode;
        elif self.data < data:
            return self.right.deleteHelper(rootNode, data);
        elif self.data > data:
            return self.left.deleteHelper(rootNode, data);

    def delete(self, data):
        self = self.deleteHelper(self, data);
        return self;

    def depthFirstSeacrh(self, dfsType):
#        Pre-Order Depth First Search
        if dfsType == 1:
            if self is not None:
                print("Node is %d and it's color is %s" % (self.data, self.color));
            if self.left is not None:
                self.left.depthFirstSeacrh(dfsType);
            if self.right is not None:
                self.right.depthFirstSeacrh(dfsType);

#         In-Order Depth First Search
        elif dfsType == 2:
            if self.left:
                self.left.depthFirstSeacrh(dfsType);
            if self:
                print("Node is %d and it's color is %s" % (self.data, self.color));
            if self.right:
                self.right.depthFirstSeacrh(dfsType);

#         Post-Order Depth First Search
        elif dfsType == 3:
            if self and self.left:
                self.left.depthFirstSeacrh(dfsType);
            if self.right:
                self.right.depthFirstSeacrh(dfsType);
            if self:
                print("Node is %d and it's color is %s" % (self.data, self.color));

"""tree = RedBlackTree(10, None, "BLACK");
tree = tree.insert(5);
tree = tree.insert(7);
tree = tree.insert(20);
tree = tree.insert(6);
tree = tree.insert(18);
tree = tree.insert(28);
tree = tree.insert(-1);
tree = tree.insert(17);
tree = tree.insert(4);
tree = tree.insert(19);
tree = tree.insert(8);
tree = tree.insert(9);
tree = tree.insert(3);

print("********PRE-ORDER********");
tree.depthFirstSeacrh(1);
print("*************************");
 
print("********IN-ORDER********");
tree.depthFirstSeacrh(2);
print("************************");

print("********POST-ORDER********");
tree.depthFirstSeacrh(3);
print("**************************");"""




tree = RedBlackTree(10, None, "BLACK");
tree.left = RedBlackTree(-30, tree, "BLACK");
tree.left.left = RedBlackTree(-40, tree.left, "BLACK");
tree.left.right = RedBlackTree(-20, tree.left, "BLACK");

tree.right = RedBlackTree(50, tree, "BLACK");
tree.right.left = RedBlackTree(30, tree.right, "RED");
tree.right.right = RedBlackTree(70, tree.right, "BLACK");

tree.right.left.left = RedBlackTree(15, tree.right.left, "BLACK");
tree.right.left.right = RedBlackTree(40, tree.right.left, "BLACK");

print("********POST-ORDER********");
tree.depthFirstSeacrh(3);
print("**************************");


print("********************Delete**********************");
tree = tree.delete(-40);
tree.depthFirstSeacrh(3); 
print("********************Delete**********************");




"""tree = RedBlackTree(10, None, "BLACK");
tree.left = RedBlackTree(-10, tree, "BLACK");

tree.right = RedBlackTree(30, tree, "BLACK");
tree.right.left = RedBlackTree(25, tree.right, "RED");
tree.right.right = RedBlackTree(40, tree.right, "RED");


print("********POST-ORDER********");
tree.depthFirstSeacrh(3);
print("**************************");


print("********************Delete**********************");
tree = tree.delete(-10);
tree.depthFirstSeacrh(3); 
print("********************Delete**********************");"""



"""tree = RedBlackTree(10, None, "BLACK");
tree.left = RedBlackTree(-10, tree, "BLACK");
tree.right = RedBlackTree(30, tree, "BLACK");


print("********POST-ORDER********");
tree.depthFirstSeacrh(3);
print("**************************");


print("********************Delete**********************");
tree = tree.delete(-10);
tree.depthFirstSeacrh(3); 
print("********************Delete**********************");"""
