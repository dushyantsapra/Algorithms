'''
Created on Aug 14, 2016

@author: Dushyant Sapra
'''

class DisjointSetNode:
    def __init__(self, data):
        self.data = data;
        self.parent = None;
        self.rank = 0;

    def setParent(self, parentNode):
        self.parent = parentNode;

    def getParent(self):
        return self.parent;

    def getData(self):
        return self.data;

    def getRank(self):
        return self.rank;

class DisjointSet:
    def __init__(self):
        self.disjointSetNodeMap = {};

    def getParent(self, data):
        if data in self.disjointSetNodeMap:
            return self.disjointSetNodeMap[data].getParent();
        else:
            return None;

    def makeSet(self, data):
        node = DisjointSetNode(data);
        node.setParent(node);
        self.disjointSetNodeMap[data] = node;

    def union(self, data1, data2):
        parent1 = self.findSet(data1);
        parent2 = self.findSet(data2);

        if parent1 == parent2:
            return False;

        if parent1.getRank() >= parent2.getRank():
            if parent1.getRank() == parent2.getRank():
                parent1.rank += 1;
            parent2.parent = parent1;
        else:
            parent1.parent = parent2;

        return True;

    def findSet(self, data):
        disjointSetNode = self.disjointSetNodeMap[data];
        if disjointSetNode.getParent() is disjointSetNode:
            return disjointSetNode;

        disjointSetNode.parent = self.findSet(disjointSetNode.getParent().getData());
        return disjointSetNode.parent;

if __name__ == '__main__': 
    s = DisjointSet();
    s.makeSet("V1");
    s.makeSet("V2");
    s.makeSet("V3");
    s.makeSet("V4");
    s.makeSet("V5");
    s.makeSet("V6");
    s.makeSet("V7");
    
    s.union("V1", "V2");
    s.union("V2", "V3");
    s.union("V4", "V5");
    s.union("V6", "V7");
    s.union("V5", "V6");
    s.union("V3", "V7");
    
    print(s.findSet("V1").getData());
    print(s.findSet("V1").getRank());
