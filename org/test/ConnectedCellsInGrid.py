'''
Created on Apr 20, 2017

@author: xdussap
'''
from os.path import os


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
        if data1 not in self.disjointSetNodeMap:
            self.makeSet(data1);
        
        if data2 not in self.disjointSetNodeMap:
            self.makeSet(data2);
        
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
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);

    rowcount = int(inputfile.readline().strip());
    colcount = int(inputfile.readline().strip());

    matrix = [];
    gridMatrix = [];
    for _ in range(rowcount):
        matrix.append(list(map(int, inputfile.readline().strip().split(" "))));
        ll = [];
        for jLoop in range(colcount):
            ll.append(set());
        gridMatrix.append(ll);

#     print(matrix)
#     print(gridMatrix)
    
    currentGrid = 1;
    for rowIndex in range(rowcount):
        for colIndex in range(colcount):
            if matrix[rowIndex][colIndex] == 1:
                gridMatrix[rowIndex][colIndex].add(currentGrid);

                for iCount in range(8):
                    if iCount == 0 and (colIndex - 1) >= 0 and matrix[rowIndex][colIndex - 1] == 1:
                        gridMatrix[rowIndex][colIndex - 1].add(currentGrid);

                    elif iCount == 1 and (colIndex - 1) >= 0 and (rowIndex - 1) >= 0 and matrix[rowIndex - 1][colIndex - 1] == 1:
                        gridMatrix[rowIndex - 1][colIndex - 1].add(currentGrid);
                    
                    elif iCount == 2 and (rowIndex - 1) >= 0 and matrix[rowIndex - 1][colIndex] == 1:
                        gridMatrix[rowIndex - 1][colIndex].add(currentGrid);
                    
                    elif iCount == 3 and (rowIndex - 1) >= 0 and (colIndex + 1) <= (colcount - 1) and matrix[rowIndex - 1][colIndex + 1] == 1:
                        gridMatrix[rowIndex - 1][colIndex + 1].add(currentGrid);
                    
                    elif iCount == 4 and (colIndex + 1) <= (colcount - 1) and matrix[rowIndex][colIndex + 1] == 1:
                        gridMatrix[rowIndex][colIndex + 1].add(currentGrid);
                    
                    elif iCount == 5 and (rowIndex + 1) <= (rowcount - 1) and (colIndex + 1) <= (colcount - 1) and matrix[rowIndex + 1][colIndex + 1] == 1: 
                        gridMatrix[rowIndex + 1][colIndex + 1].add(currentGrid);
                    
                    elif iCount == 6 and (rowIndex + 1) <= (rowcount - 1) and matrix[rowIndex + 1][colIndex] == 1:
                        gridMatrix[rowIndex + 1][colIndex].add(currentGrid);
                    
                    elif iCount == 7 and (rowIndex + 1) <= (rowcount - 1) and (colIndex - 1) >= 0 and matrix[rowIndex + 1][colIndex - 1] == 1: 
                        gridMatrix[rowIndex + 1][colIndex - 1].add(currentGrid);
                currentGrid += 1;

#     print(gridMatrix)

    disjointSet = DisjointSet();

    coordinateList = [];
    coordinateMap = {};
    for rowIndex in range(rowcount):
        for colIndex in range(colcount):
            tmpTuple = (rowIndex, colIndex)
            
            if len(gridMatrix[rowIndex][colIndex]) == 1:
                coordinateList.append(tmpTuple);
                disjointSet.union(gridMatrix[rowIndex][colIndex].pop(), tmpTuple);
            elif len(gridMatrix[rowIndex][colIndex]) > 1:
                coordinateList.append(tmpTuple);
                coordinateMap[tmpTuple] = list(gridMatrix[rowIndex][colIndex]);

    for coordinate, tmpList in coordinateMap.items():
        disjointSet.union(tmpList[0], coordinate);
        
        for iLoop in range(len(tmpList)):
            for jLoop in range(iLoop + 1, len(tmpList)):
                disjointSet.union(tmpList[iLoop], tmpList[jLoop]);
        
#     print(coordinateList)
#     print(disjointSet)

            
    
    for iLoop in range(1, currentGrid):
        disjointSet.findSet(iLoop);
    
    for tmpTuple in coordinateList:
        disjointSet.findSet(tmpTuple);
    
    tmpMap = {};
    for tmpTuple in coordinateList:
        tmpData = disjointSet.getParent(tmpTuple).getData();
        if tmpData not in tmpMap:
            tmpMap[tmpData] = 1;
        else:
            tmpMap[tmpData] += 1;
    
#     print(tmpMap)
    
    maxValue = float("-inf");
    for value in tmpMap.values():
        if maxValue < value:
            maxValue = value;
    
    print(maxValue)

