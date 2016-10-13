'''
Created on 21-Jun-2016

@author: Dushyant Sapra
'''

class AVLTree:
    def __init__(self, data):
        self.left = None;
        self.right = None;
        self.balancingFactor = 0;
        self.data = data;

    def height(self):
        lHeight = 0;
        rHeight = 0;

        if self.left:
            lHeight = self.left.height();
        if self.right:
            rHeight = self.right.height();

        return (lHeight + 1) if lHeight > rHeight else (rHeight + 1);

    def leftRotation(self):
        newNode = self.right;
        self.right = None;
        self.right = newNode.left;
        newNode.left = self;
        return newNode;

    def rightRotation(self):
        newNode = self.left;
        self.left = None;
        self.left = newNode.right;
        newNode.right = self;
        return newNode;

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

    def restoreBalance(self):
        lHeight = 0;
        rHeight = 0;
        print("Checking and Restoing Balance at %d" % (self.data));
        if self.left:
            lHeight = self.left.height();
 
        if self.right:
            rHeight = self.right.height();
 
#         Right Sub-tree is Heavy
        if (lHeight - rHeight) < -1:
            lHeight = 0;
            rHeight = 0;
            if self.right.right:
                lHeight = self.right.right.height();
            elif self.left.right:
                rHeight = self.right.left.height();

#             Right Right Case
            if lHeight > rHeight:
                self = self.leftRotation();
#             Right Left Case
            else:
                self.right = self.right.rightRotation();
                self = self.leftRotation();

#         Left Sub-tree is Heavy
        elif (lHeight - rHeight) > 1:
            lHeight = 0;
            rHeight = 0;
            if self.left.left:
                lHeight = self.left.left.height();
            elif self.left.right:
                rHeight = self.left.right.height();

#             Left Left Case
            if lHeight > rHeight:
                self = self.rightRotation();
#             Left Right Case
            else:
                self.left = self.left.leftRotation();
                self = self.rightRotation();
        return self;

    def findMinInRightSubTreeAndRestoreBalance(self):
        if self.left:
            data, self.left = self.left.findMinInRightSubTreeAndRestoreBalance();
            self = self.restoreBalance();
            return data, self;
        else:
            if self.right:
                data = self.data;
                return data, self.right;
            else:
                data = self.data;
                return data, None;

    def deleteHelper(self, data):
        if self.data == data:
            if self.right:
                data, self.right = self.right.findMinInRightSubTreeAndRestoreBalance();
                self.data = data;
                self = self.restoreBalance();
                return self;
            elif self.left:
                return self.left;
            else:
                return None;
        elif self.data < data:
            self.right = self.right.deleteHelper(data);
            self = self.restoreBalance();
            return self;
        elif self.data > data:
            self.left = self.left.deleteHelper(data);
            self = self.restoreBalance();
            return self;

    def delete(self, data):
        self = self.deleteHelper(data);
        return self;

    def insert(self, data):
        if self.data > data:
            if self.left is None:
                self.left = AVLTree(data);
            else:
                self.left = self.left.insert(data);
            self = self.restoreBalance();
        else:
            if self.right is None:
                self.right = AVLTree(data);
            else:
                self.right = self.right.insert(data);
            self = self.restoreBalance();
        return self;

    def depthFirstSeacrh(self, dfsType):
#        Pre-Order Depth First Search
        if dfsType == 1:
            if self:
                print(self.data);
            if self.left:
                self.left.depthFirstSeacrh(dfsType);
            if self.right:
                self.right.depthFirstSeacrh(dfsType);

#         In-Order Depth First Search
        elif dfsType == 2:
            if self.left:
                self.left.depthFirstSeacrh(dfsType);
            if self:
                print(self.data);
            if self.right:
                self.right.depthFirstSeacrh(dfsType);

#         Post-Order Depth First Search
        elif dfsType == 3:
            if self.left:
                self.left.depthFirstSeacrh(dfsType);
            if self.right:
                self.right.depthFirstSeacrh(dfsType);
            if self:
                print(self.data);

19, 10, 4, 7, 14, 12, 18, 46, 37, 28, 24, 32, 1, 50, 21, 27, 30, 35, 40, 38, 45
# tree = AVLTree(19);
# tree = tree.insert(10);
# tree = tree.insert(4);
# tree = tree.insert(7);
# tree = tree.insert(14);
# tree = tree.insert(12);
# tree = tree.insert(18);
# tree = tree.insert(46);
# tree = tree.insert(37);
# tree = tree.insert(28);
# tree = tree.insert(24);
# tree = tree.insert(32);
# tree = tree.insert(1);
# tree = tree.insert(50);
# tree = tree.insert(21);
# tree = tree.insert(27);
# tree = tree.insert(30);
# tree = tree.insert(35);
# tree = tree.insert(40);
# tree = tree.insert(38);
# tree = tree.insert(45);


tree = AVLTree(10);
tree = tree.insert(20);
tree = tree.insert(-5);
tree = tree.insert(4);

print("**********");
tree.depthFirstSeacrh(1);
print("**********");
  
print("**********");
tree.depthFirstSeacrh(2);
print("**********");
  
print("**********");
tree.depthFirstSeacrh(3);
print("**********");

print("********************************Deletion********************************");

# tree = tree.delete(37);
# tree = tree.delete(28);
# tree = tree.delete(40);
# tree = tree.delete(19);

tree = tree.delete(20);
print("*****D*****");
tree.depthFirstSeacrh(3);
print("*****D*****");

print("********************************Deletion********************************");


"""# 19, 10, 4, 7, 14, 12, 18, 46, 37, 28, 21, 32
tree = AVLTree(10);
tree = tree.insert(20);
tree = tree.insert(5);
tree = tree.insert(4);
tree = tree.insert(2);
print("**********");
tree.depthFirstSeacrh(1);
print("**********");
 
print("**********");
tree.depthFirstSeacrh(2);
print("**********");
 
print("**********");
tree.depthFirstSeacrh(3);
print("**********");"""
