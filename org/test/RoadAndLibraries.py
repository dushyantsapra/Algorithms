'''
Created on May 2, 2017

@author: xdussap
'''
from os.path import os


class UndrirectedGraph:
    def __init__(self, vertexCount):
        self.vertexCount = vertexCount;
        self.vertexMap = {};
        for iLoop in range(1, vertexCount + 1):
            self.vertexMap[iLoop] = [];
    
    def dfs(self, sVertex, connectedVertexCount, visitedVertexMap):
        for vertex in self.vertexMap[sVertex]:
            if vertex not in visitedVertexMap:
                connectedVertexCount[0] += 1;
                visitedVertexMap[vertex] = True;
                self.dfs(vertex, connectedVertexCount, visitedVertexMap);
    
    def getConnectedComponentWithCount(self):
        visitedVertexMap = {};
        connectedComponentsmap = {};
        currentCount = 1;
        for vertex in range(1, self.vertexCount + 1):
            if vertex not in visitedVertexMap:
                connectedVertexCount = [0];
                self.dfs(vertex, connectedVertexCount, visitedVertexMap);
                connectedComponentsmap[currentCount] = connectedVertexCount[0];
                currentCount += 1; 
        return connectedComponentsmap
    
    def calCost(self, librarybuildCost, roadbuildCost):
        connectedComponentCountMap = self.getConnectedComponentWithCount()
        totalCost = 0;
        
        for value in connectedComponentCountMap.values():
            totalCost += librarybuildCost;
            if value > 0:
                totalCost += int(roadbuildCost * (value - 1))
        return totalCost;

if __name__ == '__main__':
    path = os.path.join("C:\\Users\\xdussap\\workspace\\", "input.txt");
    inputfile = open(path);

    testCount = int(inputfile.readline().strip());
    for _ in range(testCount):
        vertexCount, edgeCount, librarybuildCost, roadbuildCost = list(map(int, inputfile.readline().strip().split(" ")));

        graph = UndrirectedGraph(vertexCount)
        
        for _ in range(edgeCount):
            u, v = list(map(int, inputfile.readline().strip().split(" ")));
            graph.vertexMap[u].append(v);
            graph.vertexMap[v].append(u);
        
        if librarybuildCost <= roadbuildCost or(edgeCount == 0):
            print(int(librarybuildCost * vertexCount)); 
            continue;
        
        totalCost = graph.calCost(librarybuildCost, roadbuildCost);
        print(totalCost)
